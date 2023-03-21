# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:12:15 2021

    Jogo de Varetas

@author: Nascimento
"""
import numpy as np


j   = 0 
ladosPar = []
n = int(input())
while n != 0:
    tam = np.zeros(n, dtype=(np.int64))
    A   = np.zeros(n, dtype=(np.int64))
    for i in range(n):
        b, a = input().split(' ')
        tam[i], A[i] = int(b), int(a)

    while sum(A) > 0:
        ladosPar.append(0)
        i = 0
        for x in A:
            if x % 2 != x: 
                A[i]   -= 2
                ladosPar[j] += 1
                
            elif x > 0: 
                A[i]   -= 1
            
            i += 1
    j += 1
    n = int(input())
    
for x in ladosPar:
    print(x//2)