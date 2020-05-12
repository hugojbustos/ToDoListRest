from django.contrib import admin
from django.contrib.auth.models import Group, User

# Register your models here.

from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','estado','adjunto')
    search_fields = ('id','descripcion','estado')
   # readonly_fields = ('id')

    filter_horizontal=()
    list_filter=()    
    fieldsets=()

admin.site.site_header='Listado de Tareas'
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Tarea,TareaAdmin)
