from django.shortcuts import render

# Create your views here.
def inicio(request):
    listaEstudiantes = ["Javier","Victor","Carlos","Joaquin"]
    return render(request,'app2/WelcomeApp2.html',{"estudiantes":listaEstudiantes})