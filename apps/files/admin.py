from django.contrib import admin
from .models import Document, Importan, Sending, Reply, Usuario, Area, areaUsr
#from .models import Sending

admin.site.register(Document)
admin.site.register(Importan)
admin.site.register(Sending)
admin.site.register(Reply)
admin.site.register(Usuario)
admin.site.register(Area)
admin.site.register(areaUsr)
