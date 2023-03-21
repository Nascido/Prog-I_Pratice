# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:20:44 2021

    Cruzando Lagos

@author: Nascimento
"""

numeroDeTrechos = int(input())
trajeto = []

for i in range(numeroDeTrechos):
    trajeto.append(input())

pulos = 0
vaiConseguir = True
geloAnterior = '-'
risco = 0

for gelo in trajeto:
    
    if risco == 2: 
        vaiConseguir = False
        break
    
    if gelo[0] == '-':
        risco = 0
        geloAnterior = '-'
        
    else:
        if geloAnterior != '-':
            risco += 1
            pulos -= 1
        
        pulos += 1
        geloAnterior = '.'
        
if vaiConseguir:
    print(pulos)
    
else:
    print('N')