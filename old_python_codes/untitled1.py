# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:22:16 2021

    Multiplicação de Matrizes

@author: Nascimento
"""
import numpy as np

tamanho =  int(input())


P, Q, R, S, X, Y = [int(x) for x in input().split()]

I, J = [int(x) for x in input().split()]

matrizA = np.zeros((tamanho, tamanho), dtype=(np.int64))
matrizB = np.zeros((tamanho, tamanho), dtype=(np.int64))

for i in range(tamanho):
    for j in range(tamanho):
        
        ElementoA = P*i + Q*j
        
        while ElementoA > X:
            ElementoA -= X
        
        matrizA[i][j] = ElementoA
        
        ElementoB = R*i + S*j
        
        while ElementoB > Y:
            ElementoB -= Y
            
        matrizB[i][j] = ElementoB
        
ElementoMatrizC = sum(matrizA[I-1, :] * matrizB[:, J-1])

print(ElementoMatrizC)