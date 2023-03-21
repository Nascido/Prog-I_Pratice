# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:21:52 2021

    Jogo de Varetas

@author: Nascimento
"""

import numpy as np


n   = int(input())
tam = np.zeros(n)
A   = np.zeros(n)
ladosPar = np.zeros(n)
j = 0

for i in range(n):
    b, a = input().split(' ')
    if int(b) == 0: break
    tam[i], A[i] = int(b), int(a)


    while sum(A) > 0:
        i = 0
        for x in A:
            if x % 2 != x: 
                A[i]   -= 2
                ladosPar[j] += 1
                
            elif x > 0: 
                A[i]   -= 1
            
            i += 1
    j += 1
    
for x in ladosPar:
    print(x//2)