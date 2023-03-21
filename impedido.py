# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:13:14 2021

    Ele está impedido

@author: Nascimento
"""

atacantes, defensores = [int(x) for x in input().split()]

impedimentosNosTestes = []

while atacantes + defensores != 0:
    impedimento = 'N'
    distanciaAtacantes  = [int(x) for x in input().split()]
    distanciaDefensores = [int(x) for x in input().split()]
    
    distanciaAtacantes  = distanciaAtacantes[:atacantes]
    distanciaDefensores = distanciaDefensores[:defensores]
    
    for i in range(atacantes):
        if distanciaAtacantes[i] == distanciaDefensores[i]:
            impedimento = 'Y'
            
    impedimentosNosTestes.append(impedimento)
            
    atacantes, defensores = [int(x) for x in input().split()]
            
for impedimento in impedimentosNosTestes:
    print(impedimento)