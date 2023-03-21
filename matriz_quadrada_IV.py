# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:17:24 2021
    
    Matriz Quadrada IV

@author: Nascimento
"""
from math import ceil, floor

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
        matriz = []
        for i in range(n_linhas):
            matriz.append([valor_inicial] * n_colunas)
        return matriz

matrizesCalculadas = []

while True:
    try:
        ordemDaMatriz  = int(input())
        matrizQuadrada = cria_matriz(ordemDaMatriz, ordemDaMatriz)
        
        maximoValorPara1s = ceil(ordemDaMatriz/3) + ordemDaMatriz//3
        minimoValorPara1s = floor(ordemDaMatriz/3)
        
        for i in range(ordemDaMatriz):
            for j in range(ordemDaMatriz):
                if i == j:
                    matrizQuadrada[i][j] = 2
                    
                elif i == (ordemDaMatriz - 1) - j:
                    matrizQuadrada[i][j] = 3
                    
                    
                
                if i >= minimoValorPara1s and i <= maximoValorPara1s and j >= minimoValorPara1s and j <= maximoValorPara1s:
                    matrizQuadrada[i][j] = 1
                    
                
                    
                if i == j and i == ordemDaMatriz//2:
                    matrizQuadrada[i][j] = 4
        
        matrizesCalculadas.append(matrizQuadrada)
   
    except EOFError:
        
        for matriz in matrizesCalculadas:
            
            ordem = len(matriz)
            
            for i in range(ordem):
                for j in range(ordem):
                    if j == ordem - 1:
                        print(matriz[i][j])
                        
                    else:
                        print(matriz[i][j], end=(''))
                        
            print('')
        
        break