# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Import Models
from .models import Estudiente

# Create your views here.

def index(request):
# 	estudientes = Estudiente.objects.all()
# 	output = ', '.join([estudiente.nombre for estudiente in estudientes])
# 	print(output)
    return HttpResponse("output")
	# views_estudientes = loader.get_template("views/estudientes.html")
	# data = Context({"estudientes": estudientes})
    # return HttpResponse(views_estudientes.render(data))