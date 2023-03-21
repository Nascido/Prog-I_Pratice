# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:06:56 2021

    Multiplicação de Matrizes (URI)

@author: Nascimento
"""

tamanho =  int(input())

P, Q, R, S, X, Y = [int(x) for x in input().split()]

I, J = [int(x) for x in input().split()]


def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

def multiplica_matriz(a, b):
    m = len(a)
    n = len(b)
    p = len(b[0])
    
    c = []
    
    for i in range(m): 
        c.append([0]*p)
        for j in range(p):
            soma = 0
            for k in range(n):
                soma += a[i][k] * b[k][j]
                
            c[i][j] = soma
            
    return c
                

matrizA = cria_matriz(tamanho, tamanho)
matrizB = cria_matriz(tamanho, tamanho)

for i in range(tamanho):
    for j in range(tamanho):
        matrizA[i][j] = (P*i + Q*j) % X
        matrizB[i][j] = (R*i + S*j) % Y
        
        
matrizC = multiplica_matriz(matrizA, matrizB)

print(matrizC[I-1][J-1])
    

