from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenidos a Django")

def nuevo(request):
    return HttpResponse("Mensjae desde Nueva ruta")
def welcome(request):
    return render(request,'app1/welcome.html',{'nombreAplicacion' : 'primera app'})