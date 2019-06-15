# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .serializers import *
# Import Models
from .models import *
import datetime
from rest_framework import status

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
        rest_list = Dentadura.objects.order_by('iddentadura')
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Diente

# Retorna todos los dientes
# {'iddiente','posicion','tipo'}
def get_dientes(request):
    if request.method == "GET":
        rest_list = Diente.objects.order_by('iddiente')
        serializer = DienteSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retorna el registro de un diente segun su id
# @params  
#   int: 'iddiente'
def get_diente(request, iddiente):
    if request.method == "GET":
        rest_list = Diente.objects.filter(iddiente=iddiente).values()
        serializer = DienteSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Dentadura

# Retorna todos los dientes de un paciente segun su idpaciente
# @params
#   int: 'idpaciente'
def get_dentadura_by_paciente(request):
    if request.method == "GET":
        rest_list = Dentadura.objects.raw('SELECT * FROM dentadura WHERE idpaciente=' + str(1))
        print(rest_list)
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retorna el registro de un diente segun su iddentadura
# @params  
#   int: 'iddentadura'
def get_dentadura(request, iddentadura):
    if request.method == "GET":
        rest_list = Dentadura.objects.filter(iddentadura=iddentadura).values()
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Paciente

# Retorna todos los datos de un paciente segun su idpaciente
# @params
#   int: 'idpaciente'
def get_paciente(request):
    if request.method == "GET":
        rest_list = Paciente.objects.raw('SELECT paciente.* FROM paciente WHERE idpaciente=' + str(1))
        print(rest_list)
        serializer = PacienteSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Ficha

# Retorna todos los dientes de un paciente segun su idpaciente
# @params
#   int: 'idpaciente'
def get_ficha_by_paciente(request):
    if request.method == "GET":
        rest_list = Dentadura.objects.raw('SELECT dentadura.*, diente.* FROM paciente LEFT JOIN dentadura ON dentadura.idpaciente=paciente.idpaciente LEFT JOIN diente ON dentadura.iddiente=diente.iddiente WHERE paciente.idpaciente=' + str(1))
        print(rest_list)
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

def post_paciente(request):
        datos = json.loads(request.body.decode('utf-8'))['value']
        data = dict()
        data['idpaciente']=datos['rut']
        data['nombre']=datos['nombre']
        data['apellido_pat']=datos['apellido_paterno']
        data['apellido_mat']=datos['apellido_materno']
        data['correo']=datos['correo']
        data['password'] = 'clave'
        data['direccion'] = datos['direccion']
        data['edad'] = '20'
        data['estado_civil'] =datos['estado_civil'] 
        data['sexo'] = datos['sexo']
        data['celular'] = datos['celular']
        data['telefono'] = datos['celular']
        data['ocupacion'] = datos['ocupacion']
        data['f_nac'] = datos['fecha_de_nacimiento']
        data['f_gen'] =datetime.datetime.now()
        serializer = PacienteSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





