# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:58:17 2021

    Soco Hulk

@author: Nascimento
"""
def propagação(posiçãoX, posiçãoY, Matriz, energiaDeProgagação):
    
    i = posiçãoX
    j = posiçãoY
    
    matriz[i][j] += energiaDeProgagação
    
    if i+1 < linhas:
        Matriz[i+1][j] +=  energiaDeProgagação - 1
        propagação(i+1, j, Matriz, energiaDeProgagação - 1)
        
    if i-1 >= 0:
        if Matriz[i-1][j] == 1:
    
    if j+1 < colunas:
        if parede[i][j+1] == 1:
        
    if j-1 >= 0:
        if parede[i][j-1] == 1:
        
    if i+1 < linhas and j+1


def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
        matriz = []
        for i in range(n_linhas):
            matriz.append([valor_inicial] * n_colunas)
        return matriz

numeroDeTestes = int(input())

while numeroDeTestes > 0:
    linhas, colunas, posiçãoX, posiçãoY = [int(x) for x in input().split()]
    
    posiçãoX -= 1
    posiçãoY -= 1
    
    parede = cria_matriz(linhas, colunas)
    
    for i in range(linhas):
        parede[i] = [int(x) for x in input().split()]
        
    energiaDeProgagação = 10
    regiõesAfetadas     = 1
    
    parede[posiçãoX, posiçãoY] += energiaDeProgagação
    
    
   
    
        if i+1 < linhas:
            if parede[i+1][j] == 1:
            
        if i-1 >= 0:
            if parede[i-1][j] == 1:
        
        if j+1 < colunas:
            if parede[i][j+1] == 1:
            
        if j-1 >= 0:
            if parede[i][j-1] == 1:
            
        if i+1 < linhas and j+1
        
        
        
        
    numeroDeTestes -= 1
        