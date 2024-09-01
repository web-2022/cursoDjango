from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import departamento, persona  #cualquier clase se debe importar


# Create your views here.
def directorio(request):
    listaDepartamentos = departamento.objects.all().order_by('id') # ordenará las filas por orden segun el Id
    listaPersonas = persona.objects.all()
    
    return render(request,'app3/directorio.html',{'listaPersonas':listaPersonas})  #lo que esta despues de la ultima coma es para PSARLO COMO CONTEXTO


def nuevoRegistro(request):
    listaDepartamentos = departamento.objects.all().order_by('id') # ordenará las filas por orden segun el Id
    if request.method == 'POST':
        nombreRegistro = request.POST.get('nombreRegistro')
        apellidoRegistro = request.POST.get('apellidoRegistro')
        numeroRegistro = request.POST.get('numeroRegistro')        
        emailRegistro = request.POST.get('emailRegistro')
        descripcionRegistro = request.POST.get('descripcionRegistro')
        depaRegistro = request.POST.get('departamentoSeleccionado')
        depaRelacionado = departamento.objects.get(id=depaRegistro)
        objPersona = persona.objects.create(
            nombre = nombreRegistro,
            apellido = apellidoRegistro,
            numero = numeroRegistro,
            email = emailRegistro,
            descripcion = descripcionRegistro,
            depaRelacionado = depaRelacionado
        )
        objPersona.save()
        return(HttpResponseRedirect(reverse('app3:directorio')))
    return render(request,'app3/nuevoRegistro.html',{'listaDepartamentos':listaDepartamentos})

def nuevoDepartamento(request):
    listaDepartamentos = departamento.objects.all().order_by('id') # variable que almacena y ordenará las filas de la tabla segun el Id
    if request.method == 'POST': #Defino la condición para la logica del formulario
        nombreDepartamento = request.POST.get('nombreDepartamento') #la variable recibe el valor del campo
        descripcionDepartamento = request.POST.get('descripcionDepartamento') #la variable recibe el valor del campo
        objDepartamento = departamento.objects.create(nombreDepartamento = nombreDepartamento,descripcionDepartamento=descripcionDepartamento) #variable donde 
        #se almacena la data creada, representa la fila recien creada en la BD
        objDepartamento.save()  #guarda el objeto
        return(HttpResponseRedirect(reverse('app3:directorio')))
    return render(request,'app3/nuevoDepartamento.html',{'listaDepartamentos':listaDepartamentos})