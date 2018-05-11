from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.core import serializers
from files.models import Document, Sending, Usuario, Reply
from files.forms import  DocumentForm, EnvioForm
from django.urls import path

def search(request):

    # si no es una peticion ajax, devolvemos error 400
    if not request.is_ajax() or request.method != "POST":
        return HttpResponseBadRequest()

    # definimos el termino de busqueda
    q = request.POST['q']

    #verificamos si el termino de busqueda es un documento de identidad
    match = re_path(r'^(?P<folio>[0-9]{2,})$', q)
    isCI = (False, True)[match != None]

    # generamos la query
    if isCI:
        users = Document.objects.filter(folio=match.groupdict()['folio'])
    else:
        users = Document.objects.filter(sender__contains=q)

    # seleccionamos las columnas que deseamos obtener para el json
    user_fields = (
        'folio',
        'sender',
        'date'
    )

    # to json!
    data = serializers.serialize('json', users, fields=user_fields)

    # eso es todo por hoy ^^
    return HttpResponse(data, content_type="application/json")