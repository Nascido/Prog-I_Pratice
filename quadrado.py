# -*- coding: utf-8 -*-
"""
Quadrado Mágico

@author: Nascimento
"""

tamanho = int(input())

matriz = []
for i in range(tamanho):
    matriz.append([int(x) for x in input().split()])
    

condição = True

soma = 0


for j in range(tamanho):
    soma += matriz[1][j]


somalinha = soma
for i in range(tamanho):
        if soma != somalinha:
            condição = False
            break
        
        somaLinha = 0
        for j in range(tamanho):
            somaLinha += matriz[i][j] 
        
somaColuna = soma       
for j in range(tamanho):
    if soma != somaColuna:
        condição = False
        break
    
    somaColuna = 0
    for i in range(tamanho):
        somaColuna += matriz[i][j]
                

somaDiagonalPrimaria = 0
somaDiagonalSecundaria = 0

for i in range(tamanho):
    somaDiagonalPrimaria += matriz[i][i]
    
for i in range(tamanho):
    somaDiagonalSecundaria +=  matriz[i][(tamanho-1) - i]
    
if soma != somaDiagonalPrimaria or soma != somaDiagonalSecundaria:
    condição = False
    
print(condição)
    
    
  