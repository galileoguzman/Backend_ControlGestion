
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
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

def envios(request,folio):
    envio = Sending.objects.all()
    documento = Document.objects.get(folio = folio)
    if request.method == 'POST':
        form = EnvioForm(request.POST,request.FILES)
        if form.is_valid(): 
           form.save()
        return redirect('index')
        
    else:
        documento = Document.objects.get(folio = folio)
        form = EnvioForm()
    return render (request, 'enviar.html',{'form':form, 'documento':documento})

def document_delete(request,folio):
    documento = Document.objects.get(folio=folio)
    if request.method == 'POST':
        documento.delete()
        return redirect('index')
    return render(request,'document_delete.html',{'documento':documento})

def buscar(request):
    
        q=request.GET.get('q','')
        results  = Document.objects.filter(description__icontains=q)
        #documento = get_object_or_404(Document,sender__icontains='q')
        
   
        results = []
        return render(request, 'buscar.html', {'results':results})

    
   #     return HttpResponse(json.dumps(usuario),content_type='application/json')
    #else:
     #   return HttpResponse("Solo Ajax")
#      ml')
def search_sender(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text=''

    articles= Document.objects.filter(folio__icontains=search_text)
    return render_to_response('ajax_search.html', {'articles':articles})



def user_edit(request):
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

#class Detalle(DetailView):
 #   model = Document

    

    #documents_name = list()

    #for files in documents:
    #	documents_name.append(files.description)

    #response_html = '<br>'.join(documents_name)

    #return HttpResponse(response_html)
