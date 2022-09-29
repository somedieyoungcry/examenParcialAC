from django.shortcuts import render
from .models import post1

# Create your views here.

def muestra_datos(request):
    consulta = post1.objects.all()
    contexto = {'data': consulta}
    return render(request, 'p1/index.html', contexto)

def suma(val):
    listSum = []
    for i in val:
        suma = i.x1 + i.x3 + i.x4
        listSum.append(suma)
    return listSum