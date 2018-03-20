from django.db import models

# -*- coding: utf-8 -*-

#from django.contrib.auth.models import User

class Usuario(models.Model): #modelo de la tabla usuarios, en caso de no usar el de Django
	#idUsr = models.IntegerField()  Django lo genera automáticamente si no lo especificamos
	nameusr = models.CharField(max_length=30, unique=True)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	user = models.CharField(max_length=30)
	def __str__(self):
		return self.nameusr

class Area(models.Model): #Aqui nombramos a las areas existentes
	#idArea = models.IntegerField()  Django lo genera automáticamente si no lo especificamos
	namearea= models.CharField(max_length=30)

class areaUsr(models.Model):
#Un usuario puede pertenecer a una o más áreas y para no hacer un usuario por área, 
#sólo elegimos a que áreas va a pertenecer
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)

class Importan(models.Model):
	nameimp = models.CharField(max_length=30)
	def __str__(self):
		return self.nameimp

class Document(models.Model):
#tomamos los datos del documento, le asignamos folio, lo describimos y se le asigna una fecha de creacion automática
	folio = models.IntegerField(primary_key = True ) #especificamos que esta es la llave principal
	sender = models.TextField(max_length=100)#quien lo envía
	description = models.TextField(max_length=1000)
	date = models.DateTimeField(auto_now_add=True) #Fecha en que se creó el documento
	importancia = models.ForeignKey(Importan,on_delete=models.CASCADE)#aqui decimos si el documento es urgente
	numshet = models.IntegerField()
	numann= models.IntegerField()
	dateexp= models.DateTimeField(auto_now_add=False)
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE)#quien lo recibió
	def __str__(self):
		return self.description
	#def __str__(self):
     #   return self.nameusr

class Sending(models.Model):
#aquí tomamos los datos con los cuales se envía
	#idTransaccion = IntegerField()  Django lo genera automáticamente si no lo especificamos
	date = models.DateTimeField(auto_now_add=True) #fecha en la que se envía
	folio = models.ForeignKey(Document, on_delete=models.CASCADE) #que documento se envía
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE) #destino
	annexes = models.FileField(upload_to='archivosenviados/')
#   annexes = models.ForeignKey(Annexes, on_delet=models.CASCADE)
   
#class Annexes(models.Model):
#	files= models.FileField(upload_to='archivosenviados/%Y')
#	document = models.ForeignKey(Sending, on_delete=models.CASCADE)

class Reply(models.Model):
	respuesta = models.TextField(max_length=1000)
	documento = models.ForeignKey(Document, on_delete=models.CASCADE) #Aqui respondemos a un documento que se nos ha enviado
	fecharespuesta = models.DateTimeField(auto_now_add = True)
	update_by = models.ForeignKey(Usuario, on_delete=models.CASCADE	) #quien lo respondió


