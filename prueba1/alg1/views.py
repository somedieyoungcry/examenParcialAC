from multiprocessing import context
from django.shortcuts import render
from p1.models import post1
import math

def algKNN(request): 
    x1 = 10
    x2 = 20
    x3 = 30
    df = post1.objects.all()
    ldis = distanciaEu(df,x1,x2,x3)
    ldis = sorted(ldis)
    contexto = zip(df,ldis)
    return render(request, 'alg1/algoritmo1.html', {'contexto':contexto})

def distanciaEu(df,x1,x2,x3):
    ldist = []
    for i in df:
        dis = (x1 - i.x1)**2+(x2 - i.x3)**2+(x3 - i.x4)**2
        raiz = round(math.sqrt(dis),4)
        ldist.append(raiz)
    return ldist