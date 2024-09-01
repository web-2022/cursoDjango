from django.urls import path, include
from . import views

app_name = 'app2' #variable local

urlpatterns = [
    
    path('',views.inicio, name='inicio'),
    
    
]