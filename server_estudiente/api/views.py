from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import AdministradorSerializer, AuthGroupSerializer, AuthGroupPermissionsSerializer, AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, AuthUserUserPermissionsSerializer, ConsultaSerializer, DentaduraSerializer, DenunciaSerializer, DetalleEnfermedadSerializer, DienteSerializer, DjangoAdminLogSerializer, DjangoContentTypeSerializer, DjangoMigrationsSerializer, DjangoSessionSerializer, EnfermedadSerializer, EstudienteSerializer, EstudienteDocumentSerializer, EstudienteValidadoSerializer, EstudienteVotacionSerializer, FichaSerializer, HorarioDisponibleSerializer, MensajeSerializer, NotificacionSerializer, PacienteSerializer, PacienteEnfermedadSerializer, PacienteTratadoSerializer, PacienteVotacionSerializer, SolicitaAtencionSerializer, TraspasoTratamientoSerializer, TratamientoSerializer, TratamientoDienteSerializer, UniversidadSerializer
from api.models import Administrador, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Consulta, Dentadura, Denuncia, DetalleEnfermedad, Diente, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Enfermedad, Estudiente, EstudienteDocument, EstudienteValidado, EstudienteVotacion, Ficha, HorarioDisponible, Mensaje, Notificacion, Paciente, PacienteEnfermedad, PacienteTratado, PacienteVotacion, SolicitaAtencion, TraspasoTratamiento, Tratamiento, TratamientoDiente, Universidad


class AdministradorAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Administrador.objects.get(pk=id)
            serializer = AdministradorSerializer(item)
            return Response(serializer.data)
        except Administrador.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Administrador.objects.get(pk=id)
        except Administrador.DoesNotExist:
            return Response(status=404)
        serializer = AdministradorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Administrador.objects.get(pk=id)
        except Administrador.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AdministradorAPIListView(APIView):

    def get(self, request, format=None):
        items = Administrador.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AdministradorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AdministradorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthGroupAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
            serializer = AuthGroupSerializer(item)
            return Response(serializer.data)
        except AuthGroup.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthGroup.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthGroupSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthGroupPermissionsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
            serializer = AuthGroupPermissionsSerializer(item)
            return Response(serializer.data)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupPermissionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupPermissionsAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthGroupPermissions.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthGroupPermissionsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthGroupPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthPermissionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
            serializer = AuthPermissionSerializer(item)
            return Response(serializer.data)
        except AuthPermission.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        serializer = AuthPermissionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthPermissionAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthPermission.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthPermissionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthUserAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
            serializer = AuthUserSerializer(item)
            return Response(serializer.data)
        except AuthUser.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
        except AuthUser.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
        except AuthUser.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthUser.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthUserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthUserGroupsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthUserGroups.objects.get(pk=id)
            serializer = AuthUserGroupsSerializer(item)
            return Response(serializer.data)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthUserGroups.objects.get(pk=id)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserGroupsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthUserGroups.objects.get(pk=id)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserGroupsAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthUserGroups.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthUserGroupsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthUserGroupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthUserUserPermissionsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=id)
            serializer = AuthUserUserPermissionsSerializer(item)
            return Response(serializer.data)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=id)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserUserPermissionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=id)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserUserPermissionsAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthUserUserPermissions.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthUserUserPermissionsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthUserUserPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ConsultaAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Consulta.objects.get(pk=id)
            serializer = ConsultaSerializer(item)
            return Response(serializer.data)
        except Consulta.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Consulta.objects.get(pk=id)
        except Consulta.DoesNotExist:
            return Response(status=404)
        serializer = ConsultaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Consulta.objects.get(pk=id)
        except Consulta.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ConsultaAPIListView(APIView):

    def get(self, request, format=None):
        items = Consulta.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ConsultaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ConsultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DentaduraAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Dentadura.objects.get(pk=id)
            serializer = DentaduraSerializer(item)
            return Response(serializer.data)
        except Dentadura.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Dentadura.objects.get(pk=id)
        except Dentadura.DoesNotExist:
            return Response(status=404)
        serializer = DentaduraSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Dentadura.objects.get(pk=id)
        except Dentadura.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DentaduraAPIListView(APIView):

    def get(self, request, format=None):
        items = Dentadura.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DentaduraSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DentaduraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DenunciaAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Denuncia.objects.get(pk=id)
            serializer = DenunciaSerializer(item)
            return Response(serializer.data)
        except Denuncia.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Denuncia.objects.get(pk=id)
        except Denuncia.DoesNotExist:
            return Response(status=404)
        serializer = DenunciaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Denuncia.objects.get(pk=id)
        except Denuncia.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DenunciaAPIListView(APIView):

    def get(self, request, format=None):
        items = Denuncia.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DenunciaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DenunciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DetalleEnfermedadAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DetalleEnfermedad.objects.get(pk=id)
            serializer = DetalleEnfermedadSerializer(item)
            return Response(serializer.data)
        except DetalleEnfermedad.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DetalleEnfermedad.objects.get(pk=id)
        except DetalleEnfermedad.DoesNotExist:
            return Response(status=404)
        serializer = DetalleEnfermedadSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DetalleEnfermedad.objects.get(pk=id)
        except DetalleEnfermedad.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DetalleEnfermedadAPIListView(APIView):

    def get(self, request, format=None):
        items = DetalleEnfermedad.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DetalleEnfermedadSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DetalleEnfermedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DienteAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Diente.objects.get(pk=id)
            serializer = DienteSerializer(item)
            return Response(serializer.data)
        except Diente.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Diente.objects.get(pk=id)
        except Diente.DoesNotExist:
            return Response(status=404)
        serializer = DienteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Diente.objects.get(pk=id)
        except Diente.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DienteAPIListView(APIView):

    def get(self, request, format=None):
        items = Diente.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DienteSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoAdminLogAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoAdminLog.objects.get(pk=id)
            serializer = DjangoAdminLogSerializer(item)
            return Response(serializer.data)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoAdminLog.objects.get(pk=id)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)
        serializer = DjangoAdminLogSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoAdminLog.objects.get(pk=id)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoAdminLogAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoAdminLog.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoAdminLogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoAdminLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoContentTypeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoContentType.objects.get(pk=id)
            serializer = DjangoContentTypeSerializer(item)
            return Response(serializer.data)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoContentType.objects.get(pk=id)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)
        serializer = DjangoContentTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoContentType.objects.get(pk=id)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoContentTypeAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoContentType.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoContentTypeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoContentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoMigrationsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoMigrations.objects.get(pk=id)
            serializer = DjangoMigrationsSerializer(item)
            return Response(serializer.data)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoMigrations.objects.get(pk=id)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)
        serializer = DjangoMigrationsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoMigrations.objects.get(pk=id)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoMigrationsAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoMigrations.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoMigrationsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoMigrationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoSessionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoSession.objects.get(pk=id)
            serializer = DjangoSessionSerializer(item)
            return Response(serializer.data)
        except DjangoSession.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoSession.objects.get(pk=id)
        except DjangoSession.DoesNotExist:
            return Response(status=404)
        serializer = DjangoSessionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoSession.objects.get(pk=id)
        except DjangoSession.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoSessionAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoSession.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoSessionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EnfermedadAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Enfermedad.objects.get(pk=id)
            serializer = EnfermedadSerializer(item)
            return Response(serializer.data)
        except Enfermedad.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Enfermedad.objects.get(pk=id)
        except Enfermedad.DoesNotExist:
            return Response(status=404)
        serializer = EnfermedadSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Enfermedad.objects.get(pk=id)
        except Enfermedad.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EnfermedadAPIListView(APIView):

    def get(self, request, format=None):
        items = Enfermedad.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EnfermedadSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EnfermedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EstudienteAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Estudiente.objects.get(pk=id)
            serializer = EstudienteSerializer(item)
            return Response(serializer.data)
        except Estudiente.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Estudiente.objects.get(pk=id)
        except Estudiente.DoesNotExist:
            return Response(status=404)
        serializer = EstudienteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Estudiente.objects.get(pk=id)
        except Estudiente.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EstudienteAPIListView(APIView):

    def get(self, request, format=None):
        items = Estudiente.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EstudienteSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EstudienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EstudienteDocumentAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = EstudienteDocument.objects.get(pk=id)
            serializer = EstudienteDocumentSerializer(item)
            return Response(serializer.data)
        except EstudienteDocument.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = EstudienteDocument.objects.get(pk=id)
        except EstudienteDocument.DoesNotExist:
            return Response(status=404)
        serializer = EstudienteDocumentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = EstudienteDocument.objects.get(pk=id)
        except EstudienteDocument.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EstudienteDocumentAPIListView(APIView):

    def get(self, request, format=None):
        items = EstudienteDocument.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EstudienteDocumentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EstudienteDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EstudienteValidadoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = EstudienteValidado.objects.get(pk=id)
            serializer = EstudienteValidadoSerializer(item)
            return Response(serializer.data)
        except EstudienteValidado.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = EstudienteValidado.objects.get(pk=id)
        except EstudienteValidado.DoesNotExist:
            return Response(status=404)
        serializer = EstudienteValidadoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = EstudienteValidado.objects.get(pk=id)
        except EstudienteValidado.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EstudienteValidadoAPIListView(APIView):

    def get(self, request, format=None):
        items = EstudienteValidado.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EstudienteValidadoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EstudienteValidadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EstudienteVotacionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = EstudienteVotacion.objects.get(pk=id)
            serializer = EstudienteVotacionSerializer(item)
            return Response(serializer.data)
        except EstudienteVotacion.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = EstudienteVotacion.objects.get(pk=id)
        except EstudienteVotacion.DoesNotExist:
            return Response(status=404)
        serializer = EstudienteVotacionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = EstudienteVotacion.objects.get(pk=id)
        except EstudienteVotacion.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EstudienteVotacionAPIListView(APIView):

    def get(self, request, format=None):
        items = EstudienteVotacion.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EstudienteVotacionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EstudienteVotacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FichaAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Ficha.objects.get(pk=id)
            serializer = FichaSerializer(item)
            return Response(serializer.data)
        except Ficha.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Ficha.objects.get(pk=id)
        except Ficha.DoesNotExist:
            return Response(status=404)
        serializer = FichaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Ficha.objects.get(pk=id)
        except Ficha.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class FichaAPIListView(APIView):

    def get(self, request, format=None):
        items = Ficha.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = FichaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = FichaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class HorarioDisponibleAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = HorarioDisponible.objects.get(pk=id)
            serializer = HorarioDisponibleSerializer(item)
            return Response(serializer.data)
        except HorarioDisponible.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = HorarioDisponible.objects.get(pk=id)
        except HorarioDisponible.DoesNotExist:
            return Response(status=404)
        serializer = HorarioDisponibleSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = HorarioDisponible.objects.get(pk=id)
        except HorarioDisponible.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HorarioDisponibleAPIListView(APIView):

    def get(self, request, format=None):
        items = HorarioDisponible.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = HorarioDisponibleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = HorarioDisponibleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MensajeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Mensaje.objects.get(pk=id)
            serializer = MensajeSerializer(item)
            return Response(serializer.data)
        except Mensaje.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Mensaje.objects.get(pk=id)
        except Mensaje.DoesNotExist:
            return Response(status=404)
        serializer = MensajeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Mensaje.objects.get(pk=id)
        except Mensaje.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MensajeAPIListView(APIView):

    def get(self, request, format=None):
        items = Mensaje.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = MensajeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class NotificacionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Notificacion.objects.get(pk=id)
            serializer = NotificacionSerializer(item)
            return Response(serializer.data)
        except Notificacion.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Notificacion.objects.get(pk=id)
        except Notificacion.DoesNotExist:
            return Response(status=404)
        serializer = NotificacionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Notificacion.objects.get(pk=id)
        except Notificacion.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class NotificacionAPIListView(APIView):

    def get(self, request, format=None):
        items = Notificacion.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = NotificacionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = NotificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PacienteAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Paciente.objects.get(pk=id)
            serializer = PacienteSerializer(item)
            return Response(serializer.data)
        except Paciente.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Paciente.objects.get(pk=id)
        except Paciente.DoesNotExist:
            return Response(status=404)
        serializer = PacienteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Paciente.objects.get(pk=id)
        except Paciente.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PacienteAPIListView(APIView):

    def get(self, request, format=None):
        items = Paciente.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PacienteSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PacienteEnfermedadAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = PacienteEnfermedad.objects.get(pk=id)
            serializer = PacienteEnfermedadSerializer(item)
            return Response(serializer.data)
        except PacienteEnfermedad.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = PacienteEnfermedad.objects.get(pk=id)
        except PacienteEnfermedad.DoesNotExist:
            return Response(status=404)
        serializer = PacienteEnfermedadSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = PacienteEnfermedad.objects.get(pk=id)
        except PacienteEnfermedad.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PacienteEnfermedadAPIListView(APIView):

    def get(self, request, format=None):
        items = PacienteEnfermedad.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PacienteEnfermedadSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PacienteEnfermedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PacienteTratadoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = PacienteTratado.objects.get(pk=id)
            serializer = PacienteTratadoSerializer(item)
            return Response(serializer.data)
        except PacienteTratado.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = PacienteTratado.objects.get(pk=id)
        except PacienteTratado.DoesNotExist:
            return Response(status=404)
        serializer = PacienteTratadoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = PacienteTratado.objects.get(pk=id)
        except PacienteTratado.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PacienteTratadoAPIListView(APIView):

    def get(self, request, format=None):
        items = PacienteTratado.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PacienteTratadoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PacienteTratadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PacienteVotacionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = PacienteVotacion.objects.get(pk=id)
            serializer = PacienteVotacionSerializer(item)
            return Response(serializer.data)
        except PacienteVotacion.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = PacienteVotacion.objects.get(pk=id)
        except PacienteVotacion.DoesNotExist:
            return Response(status=404)
        serializer = PacienteVotacionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = PacienteVotacion.objects.get(pk=id)
        except PacienteVotacion.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PacienteVotacionAPIListView(APIView):

    def get(self, request, format=None):
        items = PacienteVotacion.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PacienteVotacionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PacienteVotacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SolicitaAtencionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = SolicitaAtencion.objects.get(pk=id)
            serializer = SolicitaAtencionSerializer(item)
            return Response(serializer.data)
        except SolicitaAtencion.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = SolicitaAtencion.objects.get(pk=id)
        except SolicitaAtencion.DoesNotExist:
            return Response(status=404)
        serializer = SolicitaAtencionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = SolicitaAtencion.objects.get(pk=id)
        except SolicitaAtencion.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SolicitaAtencionAPIListView(APIView):

    def get(self, request, format=None):
        items = SolicitaAtencion.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SolicitaAtencionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SolicitaAtencionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TraspasoTratamientoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TraspasoTratamiento.objects.get(pk=id)
            serializer = TraspasoTratamientoSerializer(item)
            return Response(serializer.data)
        except TraspasoTratamiento.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TraspasoTratamiento.objects.get(pk=id)
        except TraspasoTratamiento.DoesNotExist:
            return Response(status=404)
        serializer = TraspasoTratamientoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TraspasoTratamiento.objects.get(pk=id)
        except TraspasoTratamiento.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TraspasoTratamientoAPIListView(APIView):

    def get(self, request, format=None):
        items = TraspasoTratamiento.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TraspasoTratamientoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TraspasoTratamientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TratamientoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Tratamiento.objects.get(pk=id)
            serializer = TratamientoSerializer(item)
            return Response(serializer.data)
        except Tratamiento.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Tratamiento.objects.get(pk=id)
        except Tratamiento.DoesNotExist:
            return Response(status=404)
        serializer = TratamientoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Tratamiento.objects.get(pk=id)
        except Tratamiento.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TratamientoAPIListView(APIView):

    def get(self, request, format=None):
        items = Tratamiento.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TratamientoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TratamientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TratamientoDienteAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TratamientoDiente.objects.get(pk=id)
            serializer = TratamientoDienteSerializer(item)
            return Response(serializer.data)
        except TratamientoDiente.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TratamientoDiente.objects.get(pk=id)
        except TratamientoDiente.DoesNotExist:
            return Response(status=404)
        serializer = TratamientoDienteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TratamientoDiente.objects.get(pk=id)
        except TratamientoDiente.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TratamientoDienteAPIListView(APIView):

    def get(self, request, format=None):
        items = TratamientoDiente.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TratamientoDienteSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TratamientoDienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UniversidadAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Universidad.objects.get(pk=id)
            serializer = UniversidadSerializer(item)
            return Response(serializer.data)
        except Universidad.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Universidad.objects.get(pk=id)
        except Universidad.DoesNotExist:
            return Response(status=404)
        serializer = UniversidadSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Universidad.objects.get(pk=id)
        except Universidad.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UniversidadAPIListView(APIView):

    def get(self, request, format=None):
        items = Universidad.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UniversidadSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UniversidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
