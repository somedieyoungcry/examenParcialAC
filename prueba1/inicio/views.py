from django.shortcuts import render
from .models import post1
# Create your views here.

def muestra_datos(request):
    consulta = post1.objects.all()
    LisSum = suma(consulta)
    contexto = zip(consulta, LisSum)
    return render(request, 'ini/inicio.html', {'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum
