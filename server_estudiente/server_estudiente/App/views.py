# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Import Models
from models import *

# Create your views here.

def index(request):

    return HttpResponse("Test vista 1. Bienvenido paciente ")