# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 10:09:45 2021

    Média geométrica

@author: Nascimento
"""

#numero de elementos
n = int(input())
conjunto = []

#Conjunto
for i in range(n):
    x = float(input())
    conjunto.append(x)

#Cálculo da média
media_geo = 1
for x in conjunto:
    media_geo *= x
    
media_geo **= n**-1