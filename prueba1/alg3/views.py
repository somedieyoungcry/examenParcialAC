from django.shortcuts import render
from p1.models import post1
from django.http import HttpResponse
import math
import random
import seaborn as sns
import matplotlib.pyplot as plt

def algRegLog(request):
    return render(request, 'alg3/alg3.html')

def algP1(request):
    if request.GET["k"].isdigit() and request.GET["x1"].isdigit() and request.GET["x2"].isdigit() and request.GET["x3"].isdigit():
        #k = int(request.GET["k"])
        x1 = int(request.GET["x1"])#Obtenemos valor de x1
        x2 = int(request.GET["x2"])#Obtenemos valor de x2
        b = random.randint(0, 10)#Aqui como todavia no hacemos la funcion entera, metemos un random de prueba
        consulta = post1.objects.all()
        listLog1 = funLog(x1, x2, b, consulta)
        contexto = zip(consulta, listLog1)
        return render (request, 'alg2/regLog.html', {'contexto': contexto})
    else:
        mensaje = "Error al ingresar los datos"
        return HttpResponse(mensaje)

def funLog(x1, x2, b, lista):
    listLog = []
    for i in lista: 
        listLog.append(1 / (1 + math.exp(-(x1 * i.x1 + x2 * i.x2 + b)))) #Función logística
        if listLog > 0.5: #Evaluamos, si es mayor a 0.5, entonces es 1, de lo contrario es 0
            listLog.append()
        else: 
            print("No pude entrar a la sentencia")
        sns.regplot(x = listLog, y = lista) #Graficamos la regresion
        plt.show() #Mostramos el grafico    
    return listLog


def obtenerB(lista):
    
    pass

