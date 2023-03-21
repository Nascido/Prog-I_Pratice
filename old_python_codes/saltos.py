# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:43:31 2021

    Melhor saltador

@author: Nascimento
"""

n = int(input())

melhores = []
atletas  = []

for i in range(n):
    saltos  = [w for w in input().split()]
    atletas.append(saltos[3])
    saltos.pop(3)
    maximo = 0
    for n in saltos:
        if maximo <= float(n): maximo = float(n)
        
    melhores.append(maximo)


i = 0
melhor = 0
for n in melhores:
   
    if melhor <= float(n): 
        melhor = float(n)
        atleta = i 
    i += 1
     
print(atletas[atleta])