# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:44:46 2021

    Matriz Escada

@author: Nascimento
"""
def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

linhas, colunas = [int(x) for x in input().split()]

matriz = cria_matriz(linhas, colunas)


for i in range(linhas):
    matriz[i] = [int(x) for x in input().split()]
    
matrizEscada = True
matrizZerada = False

numero_De_Zeros_LinhaAnterior = -1


for i in range(linhas):
    if not matrizEscada or matrizZerada:
        break
    
    numero_De_Zeros_LinhaAtual = 0
    
    for j in range(colunas):
        if matriz[i][j] == 0:
            numero_De_Zeros_LinhaAtual += 1
            
        else:
            break
            
    if numero_De_Zeros_LinhaAtual == colunas and not i == linhas - 1: #Caso uma linha sem ser a última seja igual a zero
        for k in range(i+1, linhas):
        
            if not matrizEscada:
                break
            
            for j in range(colunas):
                if matriz[k][j] != 0:
                    matrizEscada = False
                    matrizZerada = False
                    break
                
                else:
                    matrizZerada = True
                
                
    elif numero_De_Zeros_LinhaAtual <= numero_De_Zeros_LinhaAnterior: 
        matrizEscada = False
        
    numero_De_Zeros_LinhaAnterior = numero_De_Zeros_LinhaAtual
    
    
if matrizEscada:
    print('S')
    
else:
    print('N')