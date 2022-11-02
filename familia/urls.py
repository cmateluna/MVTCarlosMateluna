from django.urls import path
from familia import views

urlpatterns = [
    path('', views.index, name="index"),
]
