# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:09:19 2021

    O Último Analógimôn

@author: Nascimento
"""

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

registroDoTempo = []

while True:
    try:
        
        linha, coluna = [int(x) for x in input().split()]
        cidade = cria_matriz(linha, coluna)
        
        for i in range(linha):
            cidade[i] = [int(x) for x in input().split()]
        
        for i in range(linha):
            for j in range(coluna):
                if cidade[i][j] == 2:
                    posiçãoDigimon = [i, j]
                    
                if cidade[i][j] == 1:
                    posiçãoAsh = [i, j]
                    
        tempoDecorrido = 0
        while posiçãoDigimon[0] != posiçãoAsh[0] or posiçãoDigimon[1] != posiçãoAsh[1]:
            
            if posiçãoDigimon[0] > posiçãoAsh[0]:
                posiçãoAsh[0]  += 1
                tempoDecorrido += 1
            
            elif posiçãoDigimon[0] < posiçãoAsh[0]:
                posiçãoAsh[0]  -= 1
                tempoDecorrido += 1
                
            if posiçãoDigimon[1] > posiçãoAsh[1]:
                posiçãoAsh[1]  += 1
                tempoDecorrido += 1
            
            elif posiçãoDigimon[1] < posiçãoAsh[1]:
                posiçãoAsh[1]  -= 1
                tempoDecorrido += 1
                
        registroDoTempo.append(tempoDecorrido) 
            
    except EOFError:
        for cidade in registroDoTempo:
            print(cidade)
        
        break