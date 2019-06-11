# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

# Import Models
from .models import *

# Create your views here.

def index(request):
	if request.method == 'GET':
		estudiente = Estudiente.objects.all()
		return render(request, 'estudientes.html', {'estudientes': estudiente})