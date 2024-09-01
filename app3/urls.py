from django.urls import path, include
from . import views

app_name = 'app3' #variable local

urlpatterns = [
    
    path('',views.directorio, name='directorio'),
    path('nuevoRegistro/',views.nuevoRegistro,name='nuevoRegistro'),
    path('nuevoDepartamento/',views.nuevoDepartamento,name='nuevoDepartamento')
    
    
]