# -*- coding: utf-8 -*-
"""
Área Superior

@author: Nascimento
"""

operação = input()

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz


matriz = cria_matriz(12, 12)

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
        
lin  = 0
col  = 0
soma = 0
lin += 2
for i in range(12-lin):
    lin += 2
    col += 1
    for j in range(0+col,12-col):
        soma += matriz[i][j]
        
if operação == 'S':
    print(round(soma, 1))
    
if operação == 'M':
    print(round(soma/24, 1))
    