from django.shortcuts import render
from django.http import HttpResponse

from .models import Document, Sending, Usuario, Reply

def home(request):
    files = Document.objects.all()
    return render(request,'index.html',{'files': files})

def captura(request):
    # do something...
    return render(request, 'captura.html')

def buscar(request):
    # do something...
    return render(request, 'buscar.html')

def notificaciones(request):
    # do something...
    return render(request, 'notificaciones.html')

def envios(request):
	# do something
	return render(request, 'enviar.html')


    

    #documents_name = list()

    #for files in documents:
    #	documents_name.append(files.description)

    #response_html = '<br>'.join(documents_name)

    #return HttpResponse(response_html)
