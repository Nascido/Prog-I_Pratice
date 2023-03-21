# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:36:42 2021

    Escada Rolante

@author: Nascimento
"""

n     = int(input())
gasto = []
while n != 0:
    
    tempo = [int(x) for x in input().split()]
    tempo = tempo[:n]
    
    atividade = 10
    
    if n != 1:
        for i in range(n - 1):
            soma = tempo[i+1] - tempo[i]
            if soma > 10: soma = 10
            
            atividade += soma
           
    gasto.append(atividade)
    
    n = int(input())
    
    

for tempo in gasto:
    print(tempo)
