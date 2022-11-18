from django.shortcuts import render
from p1.models import post1
from django.http import HttpResponse
from statistics import mean, pvariance
import math
import random
import seaborn as sns
import matplotlib.pyplot as plt
r = []
def algBayIng(request,r):
    consulta = post1.objects.all()
    valores = obtenerValores(consulta)
    medias = calcularMedia(valores)
    varianzas = calcularVarianza(valores)
    datos = []
    for i in medias:
        t = (i,medias[i][0],varianzas[i][0],medias[i][1],varianzas[i][1],medias[i][2],varianzas[i][2])
        datos.append(t)
    if request.method == 'POST':
        entrada = request.POST
        x1 = int(entrada['x1'])
        x2 = int(entrada['x2'])
        x3 = int(entrada['x3'])
        resultados = []
        for i in datos:
            x11 = calcularProbabilidad(x1,i[1],i[2])
            x22 = calcularProbabilidad(x2,i[3],i[4])
            x33 = calcularProbabilidad(x3,i[5],i[6])
            resultados.append((i[0],((1/len(datos))*x11*x22*x33)))
        resultados.sort(key=lambda x:x[1])
        r = resultados[-1]
    return render(request,'alg2/alg2.html',{'data':datos,'Resultado':r[0]})

def vecinosCercanos(k,lista):
    lista_k = lista[:k]
    lista_knn = {}
    lista_letras = []
    for i in lista_k:
        if i[0] in lista_letras:
            lista_knn[i[0]] += 1
        else:
            lista_letras.append(i[0])
            lista_knn[i[0]] = 1

    return lista_knn

def calcularMedia(datos):
    media = {}
    for i in list(datos.keys()):
        media[i] = [round(mean(datos[i][0]),2),round(mean(datos[i][1]),2),round(mean(datos[i][2]),2)]
    return media

def calcularVarianza(datos):
    varianza = {}
    for i in list(datos.keys()):
        varianza[i] = [round(pvariance(datos[i][0]),2),round(pvariance(datos[i][1]),2),round(pvariance(datos[i][2]),2)]
    return varianza

def obtenerValores(consulta):
    valores = {}
    for i in consulta:
        if i.x2 not in valores:
            valores[i.x2] = [[i.x1],[i.x3],[i.x4]]
        else:
            valores[i.x2][0].append(i.x1)
            valores[i.x2][1].append(i.x3)
            valores[i.x2][2].append(i.x4)
    return valores

def calcularProbabilidad(muestra,media,varianza):
    if varianza == 0:
        return 0
    else:
        p = 1/math.sqrt(2*math.pi*varianza)
    exp = math.e*-(pow(muestra-media,2)/(2*varianza))
    return -(p*exp)