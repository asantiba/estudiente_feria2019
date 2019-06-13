from django.conf.urls import include, url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from django.contrib import admin
from server_estudiente.App import views

if django.VERSION[1] < 10:
  urlpatterns = patterns('',
  
    url(r'^administrador/(?P<id>[0-9]+)$', views.AdministradorAPIView.as_view()),
    url(r'^administrador/$', views.AdministradorAPIListView.as_view()),
  
    url(r'^authgroup/(?P<id>[0-9]+)$', views.AuthGroupAPIView.as_view()),
    url(r'^authgroup/$', views.AuthGroupAPIListView.as_view()),
  
    url(r'^authgrouppermissions/(?P<id>[0-9]+)$', views.AuthGroupPermissionsAPIView.as_view()),
    url(r'^authgrouppermissions/$', views.AuthGroupPermissionsAPIListView.as_view()),
  
    url(r'^authpermission/(?P<id>[0-9]+)$', views.AuthPermissionAPIView.as_view()),
    url(r'^authpermission/$', views.AuthPermissionAPIListView.as_view()),
  
    url(r'^authuser/(?P<id>[0-9]+)$', views.AuthUserAPIView.as_view()),
    url(r'^authuser/$', views.AuthUserAPIListView.as_view()),
  
    url(r'^authusergroups/(?P<id>[0-9]+)$', views.AuthUserGroupsAPIView.as_view()),
    url(r'^authusergroups/$', views.AuthUserGroupsAPIListView.as_view()),
  
    url(r'^authuseruserpermissions/(?P<id>[0-9]+)$', views.AuthUserUserPermissionsAPIView.as_view()),
    url(r'^authuseruserpermissions/$', views.AuthUserUserPermissionsAPIListView.as_view()),
  
    url(r'^consulta/(?P<id>[0-9]+)$', views.ConsultaAPIView.as_view()),
    url(r'^consulta/$', views.ConsultaAPIListView.as_view()),
  
    url(r'^dentadura/(?P<id>[0-9]+)$', views.DentaduraAPIView.as_view()),
    url(r'^dentadura/$', views.DentaduraAPIListView.as_view()),
  
    url(r'^denuncia/(?P<id>[0-9]+)$', views.DenunciaAPIView.as_view()),
    url(r'^denuncia/$', views.DenunciaAPIListView.as_view()),
  
    url(r'^detalleenfermedad/(?P<id>[0-9]+)$', views.DetalleEnfermedadAPIView.as_view()),
    url(r'^detalleenfermedad/$', views.DetalleEnfermedadAPIListView.as_view()),
  
    url(r'^diente/(?P<id>[0-9]+)$', views.DienteAPIView.as_view()),
    url(r'^diente/$', views.DienteAPIListView.as_view()),
  
    url(r'^djangoadminlog/(?P<id>[0-9]+)$', views.DjangoAdminLogAPIView.as_view()),
    url(r'^djangoadminlog/$', views.DjangoAdminLogAPIListView.as_view()),
  
    url(r'^djangocontenttype/(?P<id>[0-9]+)$', views.DjangoContentTypeAPIView.as_view()),
    url(r'^djangocontenttype/$', views.DjangoContentTypeAPIListView.as_view()),
  
    url(r'^djangomigrations/(?P<id>[0-9]+)$', views.DjangoMigrationsAPIView.as_view()),
    url(r'^djangomigrations/$', views.DjangoMigrationsAPIListView.as_view()),
  
    url(r'^djangosession/(?P<id>[0-9]+)$', views.DjangoSessionAPIView.as_view()),
    url(r'^djangosession/$', views.DjangoSessionAPIListView.as_view()),
  
    url(r'^enfermedad/(?P<id>[0-9]+)$', views.EnfermedadAPIView.as_view()),
    url(r'^enfermedad/$', views.EnfermedadAPIListView.as_view()),
  
    url(r'^estudiente/(?P<id>[0-9]+)$', views.EstudienteAPIView.as_view()),
    url(r'^estudiente/$', views.EstudienteAPIListView.as_view()),
  
    url(r'^estudientedocument/(?P<id>[0-9]+)$', views.EstudienteDocumentAPIView.as_view()),
    url(r'^estudientedocument/$', views.EstudienteDocumentAPIListView.as_view()),
  
    url(r'^estudientevalidado/(?P<id>[0-9]+)$', views.EstudienteValidadoAPIView.as_view()),
    url(r'^estudientevalidado/$', views.EstudienteValidadoAPIListView.as_view()),
  
    url(r'^estudientevotacion/(?P<id>[0-9]+)$', views.EstudienteVotacionAPIView.as_view()),
    url(r'^estudientevotacion/$', views.EstudienteVotacionAPIListView.as_view()),
  
    url(r'^ficha/(?P<id>[0-9]+)$', views.FichaAPIView.as_view()),
    url(r'^ficha/$', views.FichaAPIListView.as_view()),
  
    url(r'^horariodisponible/(?P<id>[0-9]+)$', views.HorarioDisponibleAPIView.as_view()),
    url(r'^horariodisponible/$', views.HorarioDisponibleAPIListView.as_view()),
  
    url(r'^mensaje/(?P<id>[0-9]+)$', views.MensajeAPIView.as_view()),
    url(r'^mensaje/$', views.MensajeAPIListView.as_view()),
  
    url(r'^notificacion/(?P<id>[0-9]+)$', views.NotificacionAPIView.as_view()),
    url(r'^notificacion/$', views.NotificacionAPIListView.as_view()),
  
    url(r'^paciente/(?P<id>[0-9]+)$', views.PacienteAPIView.as_view()),
    url(r'^paciente/$', views.PacienteAPIListView.as_view()),
  
    url(r'^pacienteenfermedad/(?P<id>[0-9]+)$', views.PacienteEnfermedadAPIView.as_view()),
    url(r'^pacienteenfermedad/$', views.PacienteEnfermedadAPIListView.as_view()),
  
    url(r'^pacientetratado/(?P<id>[0-9]+)$', views.PacienteTratadoAPIView.as_view()),
    url(r'^pacientetratado/$', views.PacienteTratadoAPIListView.as_view()),
  
    url(r'^pacientevotacion/(?P<id>[0-9]+)$', views.PacienteVotacionAPIView.as_view()),
    url(r'^pacientevotacion/$', views.PacienteVotacionAPIListView.as_view()),
  
    url(r'^solicitaatencion/(?P<id>[0-9]+)$', views.SolicitaAtencionAPIView.as_view()),
    url(r'^solicitaatencion/$', views.SolicitaAtencionAPIListView.as_view()),
  
    url(r'^traspasotratamiento/(?P<id>[0-9]+)$', views.TraspasoTratamientoAPIView.as_view()),
    url(r'^traspasotratamiento/$', views.TraspasoTratamientoAPIListView.as_view()),
  
    url(r'^tratamiento/(?P<id>[0-9]+)$', views.TratamientoAPIView.as_view()),
    url(r'^tratamiento/$', views.TratamientoAPIListView.as_view()),
  
    url(r'^tratamientodiente/(?P<id>[0-9]+)$', views.TratamientoDienteAPIView.as_view()),
    url(r'^tratamientodiente/$', views.TratamientoDienteAPIListView.as_view()),
  
    url(r'^universidad/(?P<id>[0-9]+)$', views.UniversidadAPIView.as_view()),
    url(r'^universidad/$', views.UniversidadAPIListView.as_view()),
  
  )
else:
  urlpatterns = [
  
    url(r'^administrador/(?P<id>[0-9]+)$', views.AdministradorAPIView.as_view()),
    url(r'^administrador/$', views.AdministradorAPIListView.as_view()),
  
    url(r'^authgroup/(?P<id>[0-9]+)$', views.AuthGroupAPIView.as_view()),
    url(r'^authgroup/$', views.AuthGroupAPIListView.as_view()),
  
    url(r'^authgrouppermissions/(?P<id>[0-9]+)$', views.AuthGroupPermissionsAPIView.as_view()),
    url(r'^authgrouppermissions/$', views.AuthGroupPermissionsAPIListView.as_view()),
  
    url(r'^authpermission/(?P<id>[0-9]+)$', views.AuthPermissionAPIView.as_view()),
    url(r'^authpermission/$', views.AuthPermissionAPIListView.as_view()),
  
    url(r'^authuser/(?P<id>[0-9]+)$', views.AuthUserAPIView.as_view()),
    url(r'^authuser/$', views.AuthUserAPIListView.as_view()),
  
    url(r'^authusergroups/(?P<id>[0-9]+)$', views.AuthUserGroupsAPIView.as_view()),
    url(r'^authusergroups/$', views.AuthUserGroupsAPIListView.as_view()),
  
    url(r'^authuseruserpermissions/(?P<id>[0-9]+)$', views.AuthUserUserPermissionsAPIView.as_view()),
    url(r'^authuseruserpermissions/$', views.AuthUserUserPermissionsAPIListView.as_view()),
  
    url(r'^consulta/(?P<id>[0-9]+)$', views.ConsultaAPIView.as_view()),
    url(r'^consulta/$', views.ConsultaAPIListView.as_view()),
  
    url(r'^dentadura/(?P<id>[0-9]+)$', views.DentaduraAPIView.as_view()),
    url(r'^dentadura/$', views.DentaduraAPIListView.as_view()),
  
    url(r'^denuncia/(?P<id>[0-9]+)$', views.DenunciaAPIView.as_view()),
    url(r'^denuncia/$', views.DenunciaAPIListView.as_view()),
  
    url(r'^detalleenfermedad/(?P<id>[0-9]+)$', views.DetalleEnfermedadAPIView.as_view()),
    url(r'^detalleenfermedad/$', views.DetalleEnfermedadAPIListView.as_view()),
  
    url(r'^diente/(?P<id>[0-9]+)$', views.DienteAPIView.as_view()),
    url(r'^diente/$', views.DienteAPIListView.as_view()),
  
    url(r'^djangoadminlog/(?P<id>[0-9]+)$', views.DjangoAdminLogAPIView.as_view()),
    url(r'^djangoadminlog/$', views.DjangoAdminLogAPIListView.as_view()),
  
    url(r'^djangocontenttype/(?P<id>[0-9]+)$', views.DjangoContentTypeAPIView.as_view()),
    url(r'^djangocontenttype/$', views.DjangoContentTypeAPIListView.as_view()),
  
    url(r'^djangomigrations/(?P<id>[0-9]+)$', views.DjangoMigrationsAPIView.as_view()),
    url(r'^djangomigrations/$', views.DjangoMigrationsAPIListView.as_view()),
  
    url(r'^djangosession/(?P<id>[0-9]+)$', views.DjangoSessionAPIView.as_view()),
    url(r'^djangosession/$', views.DjangoSessionAPIListView.as_view()),
  
    url(r'^enfermedad/(?P<id>[0-9]+)$', views.EnfermedadAPIView.as_view()),
    url(r'^enfermedad/$', views.EnfermedadAPIListView.as_view()),
  
    url(r'^estudiente/(?P<id>[0-9]+)$', views.EstudienteAPIView.as_view()),
    url(r'^estudiente/$', views.EstudienteAPIListView.as_view()),
  
    url(r'^estudientedocument/(?P<id>[0-9]+)$', views.EstudienteDocumentAPIView.as_view()),
    url(r'^estudientedocument/$', views.EstudienteDocumentAPIListView.as_view()),
  
    url(r'^estudientevalidado/(?P<id>[0-9]+)$', views.EstudienteValidadoAPIView.as_view()),
    url(r'^estudientevalidado/$', views.EstudienteValidadoAPIListView.as_view()),
  
    url(r'^estudientevotacion/(?P<id>[0-9]+)$', views.EstudienteVotacionAPIView.as_view()),
    url(r'^estudientevotacion/$', views.EstudienteVotacionAPIListView.as_view()),
  
    url(r'^ficha/(?P<id>[0-9]+)$', views.FichaAPIView.as_view()),
    url(r'^ficha/$', views.FichaAPIListView.as_view()),
  
    url(r'^horariodisponible/(?P<id>[0-9]+)$', views.HorarioDisponibleAPIView.as_view()),
    url(r'^horariodisponible/$', views.HorarioDisponibleAPIListView.as_view()),
  
    url(r'^mensaje/(?P<id>[0-9]+)$', views.MensajeAPIView.as_view()),
    url(r'^mensaje/$', views.MensajeAPIListView.as_view()),
  
    url(r'^notificacion/(?P<id>[0-9]+)$', views.NotificacionAPIView.as_view()),
    url(r'^notificacion/$', views.NotificacionAPIListView.as_view()),
  
    url(r'^paciente/(?P<id>[0-9]+)$', views.PacienteAPIView.as_view()),
    url(r'^paciente/$', views.PacienteAPIListView.as_view()),
  
    url(r'^pacienteenfermedad/(?P<id>[0-9]+)$', views.PacienteEnfermedadAPIView.as_view()),
    url(r'^pacienteenfermedad/$', views.PacienteEnfermedadAPIListView.as_view()),
  
    url(r'^pacientetratado/(?P<id>[0-9]+)$', views.PacienteTratadoAPIView.as_view()),
    url(r'^pacientetratado/$', views.PacienteTratadoAPIListView.as_view()),
  
    url(r'^pacientevotacion/(?P<id>[0-9]+)$', views.PacienteVotacionAPIView.as_view()),
    url(r'^pacientevotacion/$', views.PacienteVotacionAPIListView.as_view()),
  
    url(r'^solicitaatencion/(?P<id>[0-9]+)$', views.SolicitaAtencionAPIView.as_view()),
    url(r'^solicitaatencion/$', views.SolicitaAtencionAPIListView.as_view()),
  
    url(r'^traspasotratamiento/(?P<id>[0-9]+)$', views.TraspasoTratamientoAPIView.as_view()),
    url(r'^traspasotratamiento/$', views.TraspasoTratamientoAPIListView.as_view()),
  
    url(r'^tratamiento/(?P<id>[0-9]+)$', views.TratamientoAPIView.as_view()),
    url(r'^tratamiento/$', views.TratamientoAPIListView.as_view()),
  
    url(r'^tratamientodiente/(?P<id>[0-9]+)$', views.TratamientoDienteAPIView.as_view()),
    url(r'^tratamientodiente/$', views.TratamientoDienteAPIListView.as_view()),
  
    url(r'^universidad/(?P<id>[0-9]+)$', views.UniversidadAPIView.as_view()),
    url(r'^universidad/$', views.UniversidadAPIListView.as_view()),
  
  ]
