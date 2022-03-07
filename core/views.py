from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from .models import core

core = core()


@csrf_exempt
def index(request):

    if request.method == 'GET':

        welcomeMessage = core.randomMessage()

        return TemplateResponse(request, 'index.html', {"welcomeMessage":welcomeMessage})

@csrf_exempt
def blackhole(request):

    if request.method == 'GET':

        return TemplateResponse(request, 'blackhole.html', {"welcomeMessage":"no"})
