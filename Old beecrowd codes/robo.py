# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:50:32 2021

    Robô

@author: Nascimento
"""

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz


linhasDoPiso, colunasDoPiso = [int(x) for x in input().split()]

linhaDoRobo, colunaDoRobo = [int(x) for x in input().split()]

linhaDoRobo  -= 1
colunaDoRobo -= 1

pisoDaSala = cria_matriz(linhasDoPiso, colunasDoPiso)

for i in range(linhasDoPiso):
    pisoDaSala[i] = [int(x) for x in input().split()]
    
objetivoDoRobo = False

posiçãoPassada = (-1, -1)
while not objetivoDoRobo:
    
    i = linhaDoRobo
    j = colunaDoRobo
    
    norte = i-1 >= 0
    sul   = i+1 < linhasDoPiso
    leste = j-1 >= 0
    oeste = j+1 < colunasDoPiso
    
    posiçãoAtual = (i, j)
    achouLadrilhoPreto = False
    
    if norte:
        if pisoDaSala[i-1][j] == 1 and (i-1, j) != posiçãoPassada:
            achouLadrilhoPreto = True
            linhaDoRobo -= 1
        
    if sul and not achouLadrilhoPreto:
        if pisoDaSala[i+1][j] == 1 and (i+1, j) != posiçãoPassada:
            achouLadrilhoPreto = True
            linhaDoRobo += 1
        
    if leste and not achouLadrilhoPreto:
        if pisoDaSala[i][j-1] == 1 and (i, j-1) != posiçãoPassada:
            achouLadrilhoPreto = True
            colunaDoRobo -= 1
            
    if oeste and not achouLadrilhoPreto:
        if pisoDaSala[i][j+1] == 1 and (i, j+1) != posiçãoPassada:
            achouLadrilhoPreto = True
            colunaDoRobo += 1

    if not achouLadrilhoPreto:
        objetivoDoRobo = True
        
    posiçãoAtual   = (linhaDoRobo, colunaDoRobo)
    posiçãoPassada = (i, j)

        
for posição in posiçãoAtual:
    print(posição +1, end=(' '))
    


