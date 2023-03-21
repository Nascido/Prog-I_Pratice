# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:33:07 2021

    Maratona

@author: Nascimento
"""

postos, limite = [int(x) for x in input().split()]
distancia      = [int(x) for x in input().split()]
 
resultado = 'S'


for i in range(postos-1):
    if distancia[i+1] - distancia[i] > limite:
        resultado = 'N'
        break

print(resultado)