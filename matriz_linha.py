# -*- coding: utf-8 -*-
"""
Linha na Matriz

@author: Nascimento
"""

linha = int(input())
operação = input()

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


matriz = cria_matriz(12, 12)

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
        
        
soma = 0
for j in range(12):
        soma += matriz[linha][j]
        
soma = round(soma, 1)
if operação == 'S':
    print(soma)
    
if operação == 'M':
    print(soma/12)
    
        
        