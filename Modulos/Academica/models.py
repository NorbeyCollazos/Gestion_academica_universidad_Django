from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True, verbose_name="Código")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    duracion = models.PositiveSmallIntegerField(default=5, verbose_name="Duración")

    def __str__(self):
        txt = "{0}, (Duración: {1} año(s))"
        return txt.format(self.nombre, self.duracion)
    
    
class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True, verbose_name="DNI")
    apellidoPaterno = models.CharField(max_length=35, verbose_name="Apellido Paterno")
    apellidoMaterno = models.CharField(max_length=35, verbose_name="Apellido Materno")
    nombres = models.CharField(max_length=35, verbose_name="Nombres")
    fechaNacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Carrera")
    vigencia = models.BooleanField(default=True, verbose_name="Vigencia")
    
    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)
    

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name="Código")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    creditos = models.PositiveSmallIntegerField(verbose_name="Créditos")
    docente = models.CharField(max_length=100, verbose_name="Docente")

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)
    


class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == "F":
            letraSexo = "a"
        else:
            letraSexo = "o"
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.curso, fecMat)
    


 


