from django import forms
from django.forms import ModelForm, TextInput,Textarea, Select,NumberInput, DateInput, SelectDateWidget
from .models import Document,Usuario




class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = '__all__'
		labels = {
		'folio' : 'Folio',
		'sender' : 'Destinatario',
		'description' : 'Descripcion',
		'importancia' : 'Importancia',
		'numshet' : 'Numero de Hojas',
		'numann' : 'Numero de Anexos',
		'dateexp' : 'Fecha de Expiracion',
		'user' : 'Usuario que Reviso'	,	

		}
		widgets = {
		'folio' : forms.TextInput(attrs={'class':'col s6'}),
		'sender' : forms.TextInput(attrs={'class': 'col s6'}),
		'description' : forms.Textarea(attrs={'class': 'col s6'}),
		'importancia' : forms.Select(attrs={'class':'browser-default'}),
		'numshet' : forms.NumberInput(attrs={'class': 'col s6'}),
		'numann' : forms.NumberInput(attrs={'class': 'col s6'}),
		'dateexp' : forms.DateInput(attrs={'class': 'col s6','type' : 'date'}),
		'user' : forms.Select(attrs={'class':'browser-default'}),		

		}


