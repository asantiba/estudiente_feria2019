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

######### Estudiente #########

# Retorna todos los dientes
# return:
#   {'nombre','apellido','correo'}
def get_estudientes(request):
    estudientes = Estudiente.objects.all().values('nombre', 'apellido','correo')
    estudientes = list(estudientes)
    return JsonResponse(estudientes, safe=False)

# Retorna todos los dientes
# return:
#   {'nombre','apellido','correo'}
def get_table_estudientes(request):
    if request.method == 'GET':
        estudiente = Estudiente.objects.all().values('nombre', 'apellido','correo')
        return render(request, 'estudientes.html', {'estudientes': estudiente})

######### Diente #########

# Retorna todos los dientes
# return:
#   {'iddiente','posicion','tipo'}
def get_dientes(request):
    if request.method == "GET":
        rest_list = Diente.objects.order_by('iddiente')
        serializer = DienteSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retorna el registro de un diente segun su id
# @params:
#   int: 'iddiente'
def get_diente(request, iddiente):
    if request.method == "GET":
        rest_list = Diente.objects.filter(iddiente=iddiente).values()
        serializer = DienteSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

######### Dentadura #########

# Retorna todos los dientes de un paciente segun su idpaciente
# @params:
#   int: 'idpaciente'
def get_dentadura_by_paciente(request, idpaciente):
    if request.method == "GET":
        rest_list = Dentadura.objects.raw('SELECT * FROM dentadura WHERE idpaciente=' + idpaciente)
        print(rest_list)
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retorna el diente de una persona segun su iddiente e idpaciente
# @params:
#   int: 'iddiente'
#   int: 'idpaciente'
def get_diente_by_paciente(request, iddiente, idpaciente):
    if request.method == "GET":
        rest_list = Dentadura.objects.raw('SELECT * FROM dentadura WHERE idpaciente=' + idpaciente + ' AND iddiente=' + iddiente)
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retorna el registro de un diente segun su iddentadura
# @params:
#   int: 'iddentadura'
def get_dentadura(request, iddentadura):
    if request.method == "GET":
        rest_list = Dentadura.objects.raw('SELECT * FROM dentadura WHERE iddentadura=' + iddentadura)
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retorna la dentadura de todas las personas
# return:
#   {'iddiente','posicion','tipo'}
def get_dentaduras(request):
    if request.method == "GET":
        rest_list = Dentadura.objects.order_by('iddentadura')
        serializer = DentaduraSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

######### Paciente #########

# Retorna todos los datos de un paciente segun su idpaciente
# @params:
#   int: 'idpaciente'
def get_paciente(request, idpaciente):
    if request.method == "GET":
        rest_list = Paciente.objects.raw('SELECT paciente.* FROM paciente WHERE idpaciente=' + idpaciente)
        print(rest_list)
        serializer = PacienteSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# Crea un paciente segun sus datos enviados por post
# @params:
#   int: 'rut'
#   string: 'nombre'
#   string: 'apellido_paterno'
#   string: 'apellido_materno'
#   string: 'correo'
#   string: 'contrasena'
#   string: 'direccion'
#   string: 'edad'
#   string: 'estado_civil'
#   string: 'sexo'
#   int: 'celular'
#   int: 'telefono'
#   string: 'ocupacion'
#   string: 'f_nacimiento'
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
        data['f_gen'] = datetime.datetime.now()
        serializer = PacienteSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######### Ficha #########

# Retorna todos los dientes de un paciente segun su idpaciente
# @params
#   int: 'idpaciente'
def get_ficha_by_paciente(request, idpaciente):
    if request.method == "GET":
        rest_list = Dentadura.objects.raw('SELECT dentadura.*, diente.* FROM paciente LEFT JOIN dentadura ON dentadura.idpaciente=paciente.idpaciente LEFT JOIN diente ON dentadura.iddiente=diente.iddiente WHERE paciente.idpaciente=' + idpaciente)
        serializer = DentaduraSerializer(rest_list, many=True)
        lista_datos = serializer.data
        l_d = [dict(i) for i in lista_datos] # se transforma en una lista para poder iterar en ella
        d_d = [(i['iddiente'],i) for i in l_d] # se genera una lista de tuplas
        d = {k:v for k, v in d_d} # las tublas se vuelven un diccionario
        return JsonResponse(d, safe=False)

######### Tratamiento #########

# Retorna el tratamiento de un paciente segun su idpaciente
# @params
#   int: 'idpaciente'
def get_tratamiento_by_paciente(request, idpaciente):
    if request.method == "GET":
        tratamiento = Tratamiento.objects.raw('SELECT paciente.idpaciente, paciente.nombre as paciente, tratamiento.* FROM paciente LEFT JOIN paciente_tratado ON paciente.idpaciente=paciente_tratado.idpaciente LEFT JOIN tratamiento ON tratamiento.idtratamiento=paciente_tratado.idtratamiento WHERE paciente.idpaciente=' + idpaciente + ' LIMIT 1')
        s_tratamiento = TratamientoSerializer(tratamiento, many=True)

        tratamiento_medico = TratamientoMedico.objects.raw('SELECT tratamiento_medico.idtratamiento_medico, tratamiento_medico.trat FROM tratamiento_medico WHERE tratamiento_medico.idtratamiento_medico=1 LIMIT 1')
        s_tratamiento_medico = TratamientoMedicoSerializer(tratamiento_medico, many=True)

        s_tratamiento.data[0].update({"nombre": "Diagnostico"})
        
        # newdict={'nombre':'Diag'}
        # newdict.update(serializer.data)
        return JsonResponse(s_tratamiento.data, safe=False)





