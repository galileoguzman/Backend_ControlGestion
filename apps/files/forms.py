from django import forms
from django.forms import ModelForm, TextInput,Textarea, Select,NumberInput, DateInput, SelectDateWidget
from .models import Document,Usuario,Sending



class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = '__all__'
		labels = {
		'folio' : 'Folio',
		'sender' : 'Remitente',
		'description' : 'Descripcion',
		'importancia' : 'Importancia',
		'numshet' : 'Numero de Hojas',
		'numann' : 'Numero de Anexos',
		'dateexp' : 'Fecha de Expiracion',
		'user' : 'Usuario que Revisó'	,	

		}
		widgets = {
		'folio' : forms.TextInput(attrs={'class':'form-control'}),
		'sender' : forms.TextInput(attrs={'class': 'form-control'}),
		'description' : forms.Textarea(attrs={'class': 'form-control'}),
		'importancia' : forms.Select(attrs={'class':'form-control'}),
		'numshet' : forms.NumberInput(attrs={'class': 'form-control'}),
		'numann' : forms.NumberInput(attrs={'class': 'form-control'}),
		'dateexp' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
		'user' : forms.Select(attrs={'class':'form-control' }),		

		}

class EnvioForm(forms.ModelForm):
	class Meta:
		model = Sending
		fields = [
		'folio',
		'user',
		'annexes',

		]
		labels ={
		'folio' : 'Folio',
		'user' : 'Destinatario',
		'annexes' : 'Anexos',
		}
		widgets ={
		'folio' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa Folio' }),
		'user' : forms.CheckboxSelectMultiple(),
		'annexes' : forms.FileInput(),
		}



