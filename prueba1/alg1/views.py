from multiprocessing import context
from django.shortcuts import render
from p1.models import post1
#from alg1.templates.alg1 import *
import math
import random

def algKNN(request): 
    x1 = random.randint(1,1000)
    x2 = random.randint(1,1000)
    x3 = random.randint(1,1000)
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