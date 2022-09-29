from django.urls import path
from . import views

urlpatterns = [
    path('p1/', views.muestra_datos, name='muestra_datos'),
]