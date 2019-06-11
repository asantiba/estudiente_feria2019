# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .models import Dentadura
from .serializers import DentaduraSerializer

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

def get_dent_list(request):
    """
    Returns Json list of all Dentadura
    """
    if request.method == "GET":
        rest_list = Dentadura.objects.order_by('id')
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)
