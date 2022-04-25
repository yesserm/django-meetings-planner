from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse('Bienvenido al planificador de reuniones')

def date(request):
    return HttpResponse('Esta pagina fue mostrada el ' + str(datetime.now()))

def about(request):
    return HttpResponse('Mi nombre es Yesser Miranda')