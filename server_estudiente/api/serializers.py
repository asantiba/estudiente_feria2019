from rest_framework.serializers import ModelSerializer
from api.models import Administrador, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Consulta, Dentadura, Denuncia, DetalleEnfermedad, Diente, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Enfermedad, Estudiente, EstudienteDocument, EstudienteValidado, EstudienteVotacion, Ficha, HorarioDisponible, Mensaje, Notificacion, Paciente, PacienteEnfermedad, PacienteTratado, PacienteVotacion, SolicitaAtencion, TraspasoTratamiento, Tratamiento, TratamientoDiente, Universidad


class AdministradorSerializer(ModelSerializer):

    class Meta:
        model = Administrador
        fields = '__all__'


class AuthGroupSerializer(ModelSerializer):

    class Meta:
        model = AuthGroup
        fields = '__all__'


class AuthGroupPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'


class AuthPermissionSerializer(ModelSerializer):

    class Meta:
        model = AuthPermission
        fields = '__all__'


class AuthUserSerializer(ModelSerializer):

    class Meta:
        model = AuthUser
        fields = '__all__'


class AuthUserGroupsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserGroups
        fields = '__all__'


class AuthUserUserPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'


class ConsultaSerializer(ModelSerializer):

    class Meta:
        model = Consulta
        fields = '__all__'


class DentaduraSerializer(ModelSerializer):

    class Meta:
        model = Dentadura
        fields = '__all__'


class DenunciaSerializer(ModelSerializer):

    class Meta:
        model = Denuncia
        fields = '__all__'


class DetalleEnfermedadSerializer(ModelSerializer):

    class Meta:
        model = DetalleEnfermedad
        fields = '__all__'


class DienteSerializer(ModelSerializer):

    class Meta:
        model = Diente
        fields = '__all__'


class DjangoAdminLogSerializer(ModelSerializer):

    class Meta:
        model = DjangoAdminLog
        fields = '__all__'


class DjangoContentTypeSerializer(ModelSerializer):

    class Meta:
        model = DjangoContentType
        fields = '__all__'


class DjangoMigrationsSerializer(ModelSerializer):

    class Meta:
        model = DjangoMigrations
        fields = '__all__'


class DjangoSessionSerializer(ModelSerializer):

    class Meta:
        model = DjangoSession
        fields = '__all__'


class EnfermedadSerializer(ModelSerializer):

    class Meta:
        model = Enfermedad
        fields = '__all__'


class EstudienteSerializer(ModelSerializer):

    class Meta:
        model = Estudiente
        fields = '__all__'


class EstudienteDocumentSerializer(ModelSerializer):

    class Meta:
        model = EstudienteDocument
        fields = '__all__'


class EstudienteValidadoSerializer(ModelSerializer):

    class Meta:
        model = EstudienteValidado
        fields = '__all__'


class EstudienteVotacionSerializer(ModelSerializer):

    class Meta:
        model = EstudienteVotacion
        fields = '__all__'


class FichaSerializer(ModelSerializer):

    class Meta:
        model = Ficha
        fields = '__all__'


class HorarioDisponibleSerializer(ModelSerializer):

    class Meta:
        model = HorarioDisponible
        fields = '__all__'


class MensajeSerializer(ModelSerializer):

    class Meta:
        model = Mensaje
        fields = '__all__'


class NotificacionSerializer(ModelSerializer):

    class Meta:
        model = Notificacion
        fields = '__all__'


class PacienteSerializer(ModelSerializer):

    class Meta:
        model = Paciente
        fields = '__all__'


class PacienteEnfermedadSerializer(ModelSerializer):

    class Meta:
        model = PacienteEnfermedad
        fields = '__all__'


class PacienteTratadoSerializer(ModelSerializer):

    class Meta:
        model = PacienteTratado
        fields = '__all__'


class PacienteVotacionSerializer(ModelSerializer):

    class Meta:
        model = PacienteVotacion
        fields = '__all__'


class SolicitaAtencionSerializer(ModelSerializer):

    class Meta:
        model = SolicitaAtencion
        fields = '__all__'


class TraspasoTratamientoSerializer(ModelSerializer):

    class Meta:
        model = TraspasoTratamiento
        fields = '__all__'


class TratamientoSerializer(ModelSerializer):

    class Meta:
        model = Tratamiento
        fields = '__all__'


class TratamientoDienteSerializer(ModelSerializer):

    class Meta:
        model = TratamientoDiente
        fields = '__all__'


class UniversidadSerializer(ModelSerializer):

    class Meta:
        model = Universidad
        fields = '__all__'
