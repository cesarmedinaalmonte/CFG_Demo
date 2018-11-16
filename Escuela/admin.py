from django.contrib import admin

# Register your models here.
from Escuela.models import Escuela, Profesor


class EscuelaAdmin(admin.ModelAdmin):
    list_filter = ('nombre',)
    readonly_fields = ['pk']
    #raw_id_fields = ['owner']
    search_fields = ['nombre']

class ProfesorAdmin(admin.ModelAdmin):
    list_filter = ('escuela', )
    readonly_fields = ['pk']
    #raw_id_fields = ['owner']
    search_fields = ['nombre','apellidos']


admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(Profesor, ProfesorAdmin)