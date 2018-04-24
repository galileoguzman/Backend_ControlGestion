
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#from django.shortcuts import render, redirec, get_object_or_404
#from .forms import NewDocument
from django.urls import reverse_lazy
from .models import Document, Sending, Usuario, Reply
from .forms import  DocumentForm, EnvioForm
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@login_required
def home(request):
    form = Document.objects.all().order_by('-folio')
    contexto = {'form':form}
    return render(request,'index.html',contexto)
 
def captura(request):
    documento = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('index')
    else:
        form = DocumentForm()  
    return render (request, 'captura.html',{'form':form})

def captura_edit(request,folio):
    documento = Document.objects.get(folio=folio)
    if request.method == 'GET':
        form = DocumentForm(instance=documento)
    else:
        form = DocumentForm(request.POST,instance=documento)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'captura.html',{'form':form})

def envios(request):
    envio = Sending.objects.all()
    if request.method == 'POST':
        form = EnvioForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('index')
        
    else:
        form = EnvioForm()
    return render (request, 'enviar.html',{'form':form})


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





class DocumentList(ListView):
    model = Document
    template_name='index.html'
    ordering =['-folio']

class DocumentCreate(CreateView):
    model = Document

    template_name = 'captura.html'
    form_class = DocumentForm
    success_url = reverse_lazy('index')

class Enviocreate(CreateView): 
    model = Sending
    form_class= EnvioForm 
    template_name='enviar.html'
    success_url = reverse_lazy('index')


    

    #documents_name = list()

    #for files in documents:
    #	documents_name.append(files.description)

    #response_html = '<br>'.join(documents_name)

    #return HttpResponse(response_html)
