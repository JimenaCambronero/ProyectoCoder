
from re import template
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from AppCoder.models import Persona 

def crear_familia(request):
    template = loader.get_template("templates1.html")
    familiar_1 = Persona(nombre = 'Hugo', apellido = 'Cambronero', email = 'huguito@gmail.com', altura = 1.72, fecha_nacimiento = '1952-4-5')
    familiar_1.save()
    familiar_2 = Persona(nombre = 'Graciela', apellido = 'Lambert', email = 'grace@gmail.com', altura = 1.55, fecha_nacimiento = '1955-8-22')
    familiar_2.save() 
    familiar_3 = Persona(nombre = 'Sabrina', apellido = 'Cambronero', email = 'sabri@gmail.com',  altura = 1.67, fecha_nacimiento = '1985-6-22')
    familiar_3.save()
    familiar_4 = Persona(nombre = 'Cristian', apellido = 'del Giorgio', email = 'cristian@gmail.com', altura = 1.75, fecha_nacimiento = '1988-9-8')
    familiar_4.save()
    
    dict_de_contexto = {
        "familiar_1": familiar_1,
        "familiar_2": familiar_2,
        "familiar_3": familiar_3,
        "familiar_4": familiar_4,
    }
    
    res = template.render(dict_de_contexto)
    return HttpResponse(res)