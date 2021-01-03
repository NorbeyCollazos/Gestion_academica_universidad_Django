from django.contrib import admin
from Modulos.Academica.models import *

#configuración del panel
title = "MI UNIVERSIDAD"
subtitle = "Panel administrativo de "+title

admin.site.site_header = title #Título
admin.site.site_title = title #Subtitulo
admin.site.index_title = subtitle #Título en la página

########################################

class CarreraAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre') #para crear fitro de busqueda
    list_display = ('codigo', 'nombre', 'duracion') #para mstrar columnas

class EstudianteAdmin(admin.ModelAdmin):
    search_fields = ('dni', 'apellidoPaterno', 'apellidoMaterno', 'nombres', 'fechaNacimiento', 'carrera') #para crear fitro de busqueda
    list_display = ('dni', 'apellidoPaterno', 'apellidoMaterno', 'nombres', 'fechaNacimiento', 'sexo', 'carrera', 'vigencia') #para mstrar columnas
    list_filter = ('sexo', 'vigencia') #para filtrar

class CursoAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre', 'docente')
    list_display = ('codigo', 'nombre', 'creditos', 'docente')
    
class MatriculaAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaMatricula',) #para mostrar campos
    search_fields = ('estudiante', 'curso')
    list_display = ('estudiante', 'curso')
    list_filter = ('curso',)


# Register your models here.
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
