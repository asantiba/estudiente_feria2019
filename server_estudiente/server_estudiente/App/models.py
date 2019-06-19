# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class Administrador(models.Model):
    idadmin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrador'


class Alergia(models.Model):
    idalergia = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    alergia = models.CharField(max_length=45, blank=True, null=True)
    periodo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alergia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Consulta(models.Model):
    idconsulta = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente')
    idestudiente = models.ForeignKey('Estudiente', models.DO_NOTHING, db_column='idestudiente')
    comentario = models.TextField(blank=True, null=True)
    motivo = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'


class Dentadura(models.Model):
    iddentadura = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente')
    iddiente = models.ForeignKey('Diente', models.DO_NOTHING, db_column='iddiente')
    estado = models.CharField(max_length=200, blank=True, null=True)
    comentario_detallado = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dentadura'


class Dentograma(models.Model):
    iddentograma = models.AutoField(primary_key=True)
    iddentadura = models.ForeignKey(Dentadura, models.DO_NOTHING, db_column='iddentadura', blank=True, null=True)
    caries = models.CharField(max_length=45, blank=True, null=True)
    ubicacion = models.CharField(max_length=45, blank=True, null=True)
    actividad = models.CharField(max_length=45, blank=True, null=True)
    rxbitew = models.CharField(max_length=45, blank=True, null=True)
    tda = models.CharField(max_length=45, blank=True, null=True)
    fluorosis = models.CharField(max_length=45, blank=True, null=True)
    comentario_tda = models.CharField(max_length=100, blank=True, null=True)
    comentario_fluorosis = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dentograma'


class Denuncia(models.Model):
    iddenuncia = models.AutoField(primary_key=True)
    idestudiente = models.ForeignKey('Estudiente', models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    denuncia = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    denunciador = models.IntegerField(blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'denuncia'


class DetalleEnfermedad(models.Model):
    iddetalle_enfermedad = models.AutoField(primary_key=True)
    idenfermedad = models.ForeignKey('Enfermedad', models.DO_NOTHING, db_column='idenfermedad', blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    informacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_enfermedad'


class Diente(models.Model):
    iddiente = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    posicion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enfermedad(models.Model):
    idenfermedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermedad'


class Estudiente(models.Model):
    idestudiente = models.IntegerField(primary_key=True)
    iduniversidad = models.ForeignKey('Universidad', models.DO_NOTHING, db_column='iduniversidad', blank=True, null=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45)
    anio_carrera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiente'


class EstudienteDocument(models.Model):
    idestudiente_document = models.AutoField(primary_key=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiente_document'


class EstudienteValidado(models.Model):
    idestudiente_validado = models.AutoField(primary_key=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiente_validado'


class Ficha(models.Model):
    idficha = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente')
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    tipo_sangre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha'


class Habito(models.Model):
    idhabito = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    habito = models.CharField(max_length=45, blank=True, null=True)
    periodo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habito'


class HorarioDisponible(models.Model):
    idhorario_disponible = models.AutoField(primary_key=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    idtratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='idtratamiento', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario_disponible'


class Mensaje(models.Model):
    idmensaje = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    mensaje = models.CharField(max_length=450, blank=True, null=True)
    remitente = models.IntegerField(blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensaje'


class Notificacion(models.Model):
    idnotificacion = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    notificacion = models.CharField(max_length=200, blank=True, null=True)
    remitente = models.IntegerField(blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'


class Paciente(models.Model):
    idpaciente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido_pat = models.CharField(max_length=45, blank=True, null=True)
    apellido_mat = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    estado_civil = models.CharField(max_length=45, blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    ocupacion = models.CharField(max_length=45, blank=True, null=True)
    f_nac = models.DateTimeField(blank=True, null=True)
    f_gen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class PacienteEnfermedad(models.Model):
    idpaciente_enfermedad = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    iddetalle_enfermedad = models.ForeignKey(DetalleEnfermedad, models.DO_NOTHING, db_column='iddetalle_enfermedad', blank=True, null=True)
    f_gen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_enfermedad'


class PacienteTratado(models.Model):
    idpaciente_tratado = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    idtratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='idtratamiento', blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_tratado'


class Procedimiento(models.Model):
    idprocedimiento = models.AutoField(primary_key=True)
    procedimiento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedimiento'


class ProcedimientoTratamiento(models.Model):
    idprocedimiento_tratamiento = models.AutoField(primary_key=True)
    idprocedimiento = models.ForeignKey(Procedimiento, models.DO_NOTHING, db_column='idprocedimiento', blank=True, null=True)
    idtratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='idtratamiento', blank=True, null=True)
    procedimiento = models.CharField(max_length=45, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    descuento = models.IntegerField(blank=True, null=True)
    detalle = models.CharField(max_length=200, blank=True, null=True)
    ubicacion = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedimiento_tratamiento'


class SolicitaAtencion(models.Model):
    idsolicita_atencion = models.AutoField(primary_key=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    comentario = models.CharField(max_length=200, blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicita_atencion'


class TraspasoTratamiento(models.Model):
    idtraspaso_tratamiento = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idpaciente', blank=True, null=True)
    idtratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='idtratamiento', blank=True, null=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    comentario = models.IntegerField(blank=True, null=True)
    vigente = models.IntegerField(blank=True, null=True)
    f_gen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traspaso_tratamiento'


class Tratamiento(models.Model):
    idtratamiento = models.AutoField(primary_key=True)
    idtratamiento_medico = models.ForeignKey('TratamientoMedico', models.DO_NOTHING, db_column='idtratamiento_medico', blank=True, null=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente', blank=True, null=True)
    precio_total = models.IntegerField(blank=True, null=True)
    resultados = models.CharField(max_length=200, blank=True, null=True)
    descuento = models.IntegerField(blank=True, null=True)
    garantias = models.TextField(blank=True, null=True)
    vigente = models.IntegerField(blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento'


class TratamientoDiente(models.Model):
    idtratamiento_diente = models.AutoField(primary_key=True)
    idpaciente_tratado = models.ForeignKey(PacienteTratado, models.DO_NOTHING, db_column='idpaciente_tratado')
    iddentadura = models.ForeignKey(Dentadura, models.DO_NOTHING, db_column='iddentadura')
    procedimiento = models.CharField(max_length=200, blank=True, null=True)
    comentario = models.CharField(max_length=200, blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento_diente'


class TratamientoMedico(models.Model):
    idtratamiento_medico = models.AutoField(primary_key=True)
    trat = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    valor_referencial = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento_medico'


class Universidad(models.Model):
    iduniversidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    universidadcol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universidad'


class Votacion(models.Model):
    idvotacion = models.AutoField(primary_key=True)
    idestudiente = models.ForeignKey(Estudiente, models.DO_NOTHING, db_column='idestudiente')
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idpaciente')
    votacion = models.IntegerField(blank=True, null=True)
    votante = models.IntegerField(blank=True, null=True)
    fgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'votacion'
