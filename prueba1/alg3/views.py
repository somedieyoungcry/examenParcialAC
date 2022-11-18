from django.shortcuts import render
from p1.models import post1
from django.http import HttpResponse
from statistics import mean, pvariance
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
    

"""def algRegLog(request):
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
            X11 = calcularProbabilidad(x1,i[1],i[2])
            x22 = calcularProbabilidad(x2,i[3],i[4])
            x33 = calcularProbabilidad(x3,i[5],i[6])

            resultados.append((i[0],((1/len(datos))*X11*x22*x33)))
        
        resultados.sort(key=lambda x:x[1])
        r = resultados[-1]


    return render(request,'blog/C_Bay_ing.html',{'data':datos,'Resultado':r[0]})

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
        if i.col2 not in valores:
            valores[i.col2] = [[i.col1],[i.col3],[i.col4]]
        else:
            valores[i.col2][0].append(i.col1)
            valores[i.col2][1].append(i.col3)
            valores[i.col2][2].append(i.col4)
    return valores

def calcularProbabilidad(muestra,media,varianza):
    if varianza == 0:
        return 0
    else:
        p = 1/math.sqrt(2*math.pi*varianza)
    exp = math.e*-(pow(muestra-media,2)/(2*varianza))
    return -(p*exp)"""