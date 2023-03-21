# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:42:54 2021

    Matriz Quadrada III

@author: Nascimento
"""

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

ordemDaMatriz = int(input())
matrizesCalculadas = []


while ordemDaMatriz != 0:
    MatrizQuadrada = cria_matriz(ordemDaMatriz, ordemDaMatriz)
    
    for i in range(ordemDaMatriz):
        for j in range(ordemDaMatriz):
            MatrizQuadrada[i][j] = 2**(i + j)

    matrizesCalculadas.append(MatrizQuadrada)

    ordemDaMatriz = int(input())

contadorDasMatrizes = 0

for matriz in matrizesCalculadas:

    contadorDasMatrizes += 1
    
    ordem = len(matriz)
    maiorElemento = matriz[-1][-1]
    potencia = 10
    casasDecimaisMaiorElemento = 1
    while maiorElemento % potencia != maiorElemento:
        
        potencia *= 10
        casasDecimaisMaiorElemento += 1
   
    formatoDoPrint = ''
    for i in range(casasDecimaisMaiorElemento - 1):
        formatoDoPrint += ' '

    for i in range(ordem):
        for j in range(ordem):
            if j == ordem-1:
                
                numeroFormatado = formatoDoPrint + str(matriz[i][j])
                print(numeroFormatado[-casasDecimaisMaiorElemento:])
                
            else:
                numeroFormatado = formatoDoPrint + str(matriz[i][j])
                print(numeroFormatado[-casasDecimaisMaiorElemento:], end=(' '))

    if contadorDasMatrizes != len(matrizesCalculadas):
        print('')
    