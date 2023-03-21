# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:16:49 2021

    Área Inferior

@author: Nascimento
"""
def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

ordem = 12
operação = input()

matriz   = cria_matriz(ordem, ordem)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = float(input())
        
valoresAreaInferior = []


corteDireito  = 0
corteEsquerdo = 0
for i in range(ordem-1, ordem//2, -1):
    corteDireito  += 1
    corteEsquerdo += 1
    for j in range(0 + corteEsquerdo, ordem - corteDireito):
        valoresAreaInferior.append(matriz[i][j])
        
quantidadesDeValores = len(valoresAreaInferior)
        
if operação == 'S':
    print(sum(valoresAreaInferior))
    
else:
    print(sum(valoresAreaInferior)/quantidadesDeValores)


