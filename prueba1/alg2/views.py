from django.shortcuts import render
from p1.models import post1
from django.http import HttpResponse
import math 
import numpy as np
from sklearn.naive_bayes import GaussianNB

def algBayIng(request):
    return render(request, 'alg2/algoritmo2.html')

def classBaye(request):
    if request.GET["x1"].isdigit() and request.GET["x2"].isdigit() and request.GET["x3"].isdigit():
        x1 = int(request.GET["x1"])
        x2 = int(request.GET["x2"])
        x3 = int(request.GET["x3"])
        consulta = post1.objects.all()
        media = media(request, consulta)
        varianza = varianza(request, consulta)
        equivalente = varEquivalente(consulta)
        contexto = zip(media, varianza, equivalente)
        contexto = sorted(contexto)
        contado = contar(contexto, k)
        referencia = refe(contexto, contado, k)
        mensaje = referencia
        return render(request, 'alg2/rBayeIng.html', {'resultado': referencia})
    else:
        mensaje = "Error en los datos"
    return HttpResponse(mensaje)

def media(request, lista):
    lisMedia = []
    for i in lista: 
        media1 = np.mean(i.x1)
        media2 = np.mean(i.x3)
        media3 = np.mean(i.x4)
        lisMedia.append(media1, media2, media3)
    return lisMedia

def varianza(request, lista):
    lisVar = []
    for i in lista:
        var1 = np.var(i.x1)
        var2 = np.var(i.x3)
        var3 = np.var(i.x4)
        lisVar.append(var1, var2, var3)
    return lisVar

def varEquivalente(consulta):
    equivalente = []
    for x in consulta:
        equivalente.append(x.x2)
    return equivalente

def contar(contexto, k):
    contadores = []
    y = 0
    for dist, variable in contexto:
        if y < k:
            z = 0
            cont = 0
            for dist, band in contexto:
                if z < k:
                    if variable == band:
                        cont = cont + 1
                else:
                    break
                z = z + 1
            contadores.append(cont)
        else:
            break
        y = y + 1
    return contadores

def refe(contexto, contado, k):
    cont = 0
    maxi = 0 
    variable = ''
    for equiv, i in zip(contexto, contado):
        if i > maxi and cont < k:
            maxi = i
            variable = equiv[1]
        elif cont == k-1:
            break
        cont = cont + 1
    return variable