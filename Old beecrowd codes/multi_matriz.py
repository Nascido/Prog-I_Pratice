# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:46:04 2021

    Multiplicação de Matrizes (URI)

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
        matrizA[i][j] = (P*i + Q*j) * X
        matrizB[i][j] = (R*i + S*j) * Y
        
        
matrizC = matrizA @ matrizB

print(matrizC[I-1][J-1])




