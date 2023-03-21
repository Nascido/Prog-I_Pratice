# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:24:45 2021

    Maior valor de uma sequência e sua posição

@author: Nascimento
"""

tamanho = int(input())

lista = []

for i in range(tamanho):
    lista.append(int(input()))
    
i = 0
maximo = 0
for n in lista:
    i += 1
    if maximo <= n: 
        maximo = n
        posi   = i 
    
print(maximo, posi)