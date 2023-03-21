# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 10:42:46 2021

    Cálculo de desvio padrão

@author: Nascimento
"""
from math import sqrt

#numero de elementos
n = int(input())
conjunto = []

#Conjunto
for i in range(n):
    x = float(input())
    conjunto.append(x)
    
    
#Media Aritimética
media = 0
for x in conjunto:
    media += x
    
media /= n

#Desvio Padrão 
desvio = 0
i = 0
for x in conjunto:
    i += 1
    desvio += (x - media)**2
    
desvio = sqrt(desvio/(n-1))

print(desvio)