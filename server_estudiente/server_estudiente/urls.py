"""server_estudiente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from server_estudiente.App import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^estudientes/', views.estudientes, name='estudientes'),
    url(r'^get_dent_list/', views.get_dent_list, name='get_dent_list'),

    # Url Diente
    url(r'^get_dientes/', views.get_dientes, name='get_dientes'),
    url(r'^get_diente/(?P<iddiente>\d+)/$', views.get_diente, name='get_diente'),

    # Url Dentadura
    url(r'^get_dentadura_by_paciente/', views.get_dentadura_by_paciente, name='get_dentadura_by_paciente'),
    url(r'^get_dentadura/(?P<iddentadura>\d+)/$', views.get_dentadura, name='get_dentadura'),

    # Url Paciente
    url(r'^get_paciente/', views.get_paciente, name='get_paciente'),

    # Url Ficha
    url(r'^get_ficha_by_paciente/', views.get_ficha_by_paciente, name='get_ficha_by_paciente'),

    # Post Paciente

    url(r'post_paciente/',views.post_paciente, name= 'post_paciente'),

    # Url Admin
    url(r'^admin/', admin.site.urls),
]
