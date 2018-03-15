from django.db import models

# -*- coding: utf-8 -*-

#from django.contrib.auth.models import User

class Usuario(models.Model): #modelo de la tabla usuarios, en caso de no usar el de Django
	#idUsr = models.IntegerField()  Django lo genera automáticamente si no lo especificamos
	mame = models.CharField(max_length=30, unique=True)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	user = models.CharField(max_length=30)

class Zona(models.Model): #Aqui nombramos a las areas existentes
	#idArea = models.IntegerField()  Django lo genera automáticamente si no lo especificamos
	nameArea= models.CharField(max_length=30)

class areaUsr(models.Model):
#Un usuario puede pertenecer a una o más áreas y para no hacer un usuario por área, 
#sólo elegimos a que áreas va a pertenecer
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nameArea = models.ForeignKey(Zona, on_delete=models.CASCADE)

class Prioridad(models.Model):
	namePri = models.CharField(max_length=30)

class Documento(models.Model):
#tomamos los datos del documento, le asignamos folio, lo describimos y se le asigna una fecha de creacion automática
	folio = models.IntegerField(primary_key = True ) #especificamos que esta es la llave principal
	Remitente = models.TextField(max_length=100)#quien lo envía
	descripcion = models.TextField(max_length=1000)
	date = models.DateTimeField(auto_now_add=True) #Fecha en que se creó el documento
	namePri = models.ForeignKey(Prioridad, on_delete=models.CASCADE)#aqui decimos si el documento es urgente
	numHojas = models.IntegerField()
	anexos = models.IntegerField()
	fechaExpiracion = models.DateTimeField(auto_now_add=False)
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE)#quien lo recibió


class Envio(models.Model):
#aquí tomamos los datos con los cuales se envía
	#idTransaccion = IntegerField()  Django lo genera automáticamente si no lo especificamos
	date = models.DateTimeField(auto_now_add=True) #fecha en la que se envía
	folio = models.ForeignKey(Documento, on_delete=models.CASCADE) #que documento se envía
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE) #destino
	anexos = models.FileField(upload_to='archivosenviados/%Y')

class Respuesta(models.Model):
	respuesta = models.TextField(max_length=1000)
	documento = models.ForeignKey(Envio, on_delete=models.CASCADE) #Aqui respondemos a un documento que se nos ha enviado
	fecharespuesta = models.DateTimeField(auto_now_add = True)
	update_by = models.ForeignKey(Usuario, on_delete=models.CASCADE	) #quien lo respondió


