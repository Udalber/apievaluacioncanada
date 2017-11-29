from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('base/base.html')
    context = {}
    return render(request,'base/base.html')

def elegir(request):
    template = loader.get_template('evaluacion/evaluacion.html')
    context = {}
    return render(request,'evaluacion/evaluacion.html')



