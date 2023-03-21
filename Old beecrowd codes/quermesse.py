# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 09:36:25 2021

    Quermesse

@author: Nascimento
"""

n     = int(input())
teste = 0

while n != 0:
    teste += 1
    ingressos = [int(x) for x in input().split()]
    ingressos = ingressos[:n]
    
    i = 0
    for x in ingressos:
        i += 1
        if x == i: 
            print(f'Teste {teste}\n{i}\n')
            break
    
    
    n = int(input())