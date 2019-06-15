from rest_framework import serializers
from .models import *

class AdministradorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Administrador
        fields = '__all__'


class AuthGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthGroup
        fields = '__all__'


class AuthGroupPermissionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'


class AuthPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthPermission
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = '__all__'


class AuthUserGroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUserGroups
        fields = '__all__'


class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'


class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = '__all__'


class DentaduraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dentadura
        fields = '__all__'


class DenunciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Denuncia
        fields = '__all__'


class DetalleEnfermedadSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleEnfermedad
        fields = '__all__'


class DienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diente
        fields = '__all__'


class DjangoAdminLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoAdminLog
        fields = '__all__'


class DjangoContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoContentType
        fields = '__all__'


class DjangoMigrationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoMigrations
        fields = '__all__'


class DjangoSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoSession
        fields = '__all__'


class EnfermedadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enfermedad
        fields = '__all__'


class EstudienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudiente
        fields = '__all__'


class EstudienteDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstudienteDocument
        fields = '__all__'


class EstudienteValidadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstudienteValidado
        fields = '__all__'


class EstudienteVotacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstudienteVotacion
        fields = '__all__'


class FichaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ficha
        fields = '__all__'


class HorarioDisponibleSerializer(serializers.ModelSerializer):

    class Meta:
        model = HorarioDisponible
        fields = '__all__'


class MensajeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mensaje
        fields = '__all__'


class NotificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notificacion
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = '__all__'


class PacienteEnfermedadSerializer(serializers.ModelSerializer):

    class Meta:
        model = PacienteEnfermedad
        fields = '__all__'


class PacienteTratadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PacienteTratado
        fields = '__all__'


class PacienteVotacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PacienteVotacion
        fields = '__all__'


class SolicitaAtencionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitaAtencion
        fields = '__all__'


class TraspasoTratamientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TraspasoTratamiento
        fields = '__all__'


class TratamientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tratamiento
        fields = '__all__'


class TratamientoDienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TratamientoDiente
        fields = '__all__'


class UniversidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Universidad
        fields = '__all__'
