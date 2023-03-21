# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:40:47 2021

    Praias de Florianópolis

@author: Nascimento
"""
n = int(input())

praia = []
distancia = []

for i in range(n):
    praia.append(0)
    distancia.append(0)

for i in range(n):  
    praia[i], distancia[i] = input().split(';')
    distancia[i] = float(distancia[i])

i      = 0
maximo = 0
raio   = 0
for j in distancia:
    i += 1
    if maximo <= j: 
        maximo = j
        posi   = i 
        
    if n >= 15 and n <= 20:
        raio += 1
        
media = round(sum(distancia)/float(n), 1)

print(praia[posi - 1], end=(';'))
print(raio, end=(';'))
print(media, end=(''))