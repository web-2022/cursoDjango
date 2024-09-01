from django.db import models

# Create your models here.
class departamento(models.Model):  #Creando la tabla departamento
    nombreDepartamento=models.CharField(max_length=50, null=True, blank=True)
    descripcionDepartamento=models.CharField(max_length=300, null=True, blank=True)
   

class persona(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    numero = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)

    #Relacionando tablas
    #1. Creando

    depaRelacionado = models.ForeignKey(departamento, null=True, blank=True, on_delete=models.SET_NULL)

    #2.Python manage.py makemigrations y python manage.py migrate
    #3. vamos views