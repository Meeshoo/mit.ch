from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from .models import scores


@csrf_exempt
def index(request):

    if request.method == 'GET':

        pageTitle = "Home"

        return TemplateResponse(request, 'index.html', {"pageTitle":pageTitle})

@csrf_exempt
def about(request):

    if request.method == 'GET':

        pageTitle = "About Me"

        return TemplateResponse(request, 'index.html', {"pageTitle":pageTitle})

@csrf_exempt
def projects(request):

    if request.method == 'GET':

        pageTitle = "Projects"

        return TemplateResponse(request, 'index.html', {"pageTitle":pageTitle})