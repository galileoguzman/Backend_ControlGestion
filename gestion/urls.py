"""gestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from files import views


urlpatterns = [
    url(r'^$', views.home, name='index'),
    path('admin/', admin.site.urls),
    url(r'^capturar/', views.captura, name='captura'),
    url(r'^captura_edit/(?P<folio>\d+)/$', views.captura_edit, name='captura_edit'),
    url(r'^document_delete/(?P<folio>\d+)/$', views.document_delete, name='document_delete'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^notificaciones/$', views.notificaciones, name='notificaciones'),
    url(r'^enviar/$', views.Enviocreate.as_view(), name='enviar'),

]

# ADDED STATIC AND MEDIA URLS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)