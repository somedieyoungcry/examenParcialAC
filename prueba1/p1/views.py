from django.shortcuts import render
from .models import post1

# Create your views here.

def muestra_datos(request):
    consulta = post1.objects.all()
    LisSum = suma(consulta)
    contexto = zip(consulta, LisSum)
    return render(request, 'p1/index.html', {'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum

"""def (request):
    posts = genNum.objects.all()
    dic = {'valores': posts}
    sumas = []
    for post in posts:
        suma = 0
        suma = post.val1 + post.val3 + post.val4
        sumas.append(suma)
    dic["sumas"] = sumas
    return render(request, 'blog/index.html', dic)"""
