from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.shortcuts import render, redirec, get_object_or_404
#from .forms import NewDocument
from django.urls import reverse_lazy
from .models import Document, Sending, Usuario, Reply
from .forms import  DocumentForm
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

def home(request):
    files = Document.objects.all().order_by('folio')
    return render(request,'index.html',{'files': files})

def captura(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = DocumentForm()
    return render (request, 'captura.html',{'form1':form})

def captura_edit(request,folio):
    documento = Document.objects.get(folio=folio)
    if request.method == 'GET':
        form = DocumentForm(instance=documento)
    else:
        form = DocumentForm(request.POST,instance=documento)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'captura.html',{'form1':form})

def document_delete(request,folio):
    documento = Document.objects.get(folio=folio)
    if request.method == 'POST':
        documento.delete()
        return redirect('index')
    return render(request,'document_delete.html',{'documento':documento})

def buscar(request):
    # do something...
    return render(request, 'buscar.html')

def notificaciones(request):
    # do something...
    return render(request, 'notificaciones.html')

def envios(request):
	# do something
	return render(request, 'enviar.html')


class DocumentList(ListView):
    model = Document
    template_name='index.html'

class Documentcreate(CreateView):
    model = Document
    form_class= DocumentForm 
    template_name='captura.html'
    succes_url = reverse_lazy('index')


    

    #documents_name = list()

    #for files in documents:
    #	documents_name.append(files.description)

    #response_html = '<br>'.join(documents_name)

    #return HttpResponse(response_html)
