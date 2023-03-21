# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:59:05 2021

    Campos De Minhocas

@author: Nascimento
"""

NumeroDeLinhas, NumeroDeColunas = [int(x) for x in input().split()]

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

CampoDeMinhocas = cria_matriz(NumeroDeLinhas, NumeroDeColunas)

for i in range(NumeroDeLinhas):
    CampoDeMinhocas[i] = [int(x) for x in input().split()]
    
somasDasLinhas  = []
somasDasColunas = []


somaLinha  = 0 
for i in range(NumeroDeLinhas):
    for j in range(NumeroDeColunas):
         somaLinha += CampoDeMinhocas[i][j]
         
    somasDasLinhas.append(somaLinha)
    somaLinha  = 0
    
somaColuna = 0
for j in range(NumeroDeColunas):
    for i in range(NumeroDeLinhas):
        somaColuna += CampoDeMinhocas[i][j]
        
    somasDasColunas.append(somaColuna)
    somaColuna = 0
    
print(max(max(somasDasLinhas, key = int), max(somasDasColunas, key = int)))