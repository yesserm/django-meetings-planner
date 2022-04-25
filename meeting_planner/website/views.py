from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse('Bienvenido al planificador de reuniones')