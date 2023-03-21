# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:11:08 2021

    Segundo menor valor de uma sequência

@author: Nascimento
"""


tamanho = int(input())

lista = []
for n in range(tamanho):
    lista.append(int(input()))
    
minimo = min(lista)

lista2 = []

for n in lista:
    if n > minimo:
        lista2.append(n)
    
if len(lista2) == 0: lista2.append(minimo)

print(min(lista2))