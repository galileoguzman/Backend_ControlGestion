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

from files import views 
from ajax import views as ajax_view

from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
 
urlpatterns = [
    url(r'^$', views.home, name='index'),
    path('admin/', admin.site.urls),
    url(r'^capturar/', views.captura, name='captura'),
    url(r'^captura_edit/(?P<folio>\d+)/$', views.captura_edit, name='captura_edit'),
    url(r'^document_delete/(?P<folio>\d+)/$', views.document_delete, name='document_delete'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    #url(r'^notificaciones/$', views.notificaciones, name='notificaciones'),
    url(r'^enviar/(?P<folio>\d+)/$', views.envios , name='enviar'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^search/$', views.search_sender),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

]

# ADDED STATIC AND MEDIA URLS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)