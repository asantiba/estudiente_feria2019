# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json

# Import Models
from .models import *

# Views
def index(request):
	if request.method == 'GET':
		estudiente = Estudiente.objects.all().values('nombre', 'apellido','correo')
		return render(request, 'estudientes.html', {'estudientes': estudiente})

def estudientes(request):
	estudientes = Estudiente.objects.all().values('nombre', 'apellido','correo')
	estudientes = list(estudientes)
	return JsonResponse(estudientes, safe=False)
