# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:18:44 2021

    Pão de Queijo

@author: Nascimento
"""
def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

registroDostabuleiros = []


while True:
    try:
        
        linha, coluna = [int(x) for x in input().split()]
        posiçoesDoPão = cria_matriz(linha, coluna)
        tabuleiro     = cria_matriz(linha, coluna)
        
        for i in range(linha):
            posiçoesDoPão[i] = [int(x) for x in input().split()]
        
        for i in range(linha):
            for j in range(coluna):
                if posiçoesDoPão[i][j] == 1:
                    tabuleiro[i][j] = 9
                    
                else:
                    pãesVizinhos = 0
                    if i+1 < linha:
                        if posiçoesDoPão[i+1][j] == 1: pãesVizinhos += 1
                        
                    if i-1 >= 0:
                        if posiçoesDoPão[i-1][j] == 1: pãesVizinhos += 1
                    
                    if j+1 < coluna:
                        if posiçoesDoPão[i][j+1] == 1: pãesVizinhos += 1
                        
                    if j-1 >= 0:
                        if posiçoesDoPão[i][j-1] == 1: pãesVizinhos += 1
                    
                    tabuleiro[i][j] = pãesVizinhos
                    
        registroDostabuleiros.append(tabuleiro)
       
    except EOFError:
        for tabuleiro in registroDostabuleiros:
            
            linha  = len(tabuleiro)
            coluna = len(tabuleiro[0])
            
            for i in range(linha):
                for j in range(coluna):
                    if j == coluna - 1:
                        print(tabuleiro[i][j])
                        
                    else:
                        print(tabuleiro[i][j], end=(''))
                        
            print('')
        
        break
