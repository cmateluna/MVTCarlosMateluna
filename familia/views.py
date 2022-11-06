from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from familia.models import Persona
from familia.forms import PersonaForm

# Create your views here.

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/listado_familiares.html')
    context = {
        'personas': personas,
    }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request)) 

def agregar(request):
    # '''
    # TODO: agregar un mensaje en el template index.html que avise al usuario que 
    # la persona fue cargada con éxito
    # '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento).save()

            return HttpResponseRedirect(reverse("index"))
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})    