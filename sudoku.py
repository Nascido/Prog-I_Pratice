# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 08:29:48 2021

    Sudoku

@author: Nascimento
"""
numeroDeJogos          = int(input()) 
resultadoDasInstancias = []
def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

for i in range(numeroDeJogos):
    resultadoDasInstancias.append(False)


for jogadas in range (numeroDeJogos):
    jogadaDeSudoku = cria_matriz(9, 9, valor_inicial= '')
    for linha in range(9):
        jogadaDeSudoku[linha] = [int(x) for x in input().split()]
        
     
    
    QuebrouARegra = False
    for i in range(9):
        
        sequenciaParaLinhas  = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
        sequenciaParaColunas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        if QuebrouARegra:
            break
        
        for j in range(9):
            if jogadaDeSudoku[i][j] in sequenciaParaLinhas and jogadaDeSudoku[j][i] in sequenciaParaColunas:
                
                posiçãoParaLinhas  = sequenciaParaLinhas.index(jogadaDeSudoku[i][j])
                sequenciaParaLinhas.pop(posiçãoParaLinhas)
                
                posiçãoParaColunas = sequenciaParaColunas.index(jogadaDeSudoku[j][i])
                sequenciaParaColunas.pop(posiçãoParaColunas)
                
            else:
                QuebrouARegra = True
                resultadoDasInstancias[jogadas] = True
                
                break
                
for jogada in range(numeroDeJogos):
    
    print(f'Instancia {jogada+1}')
    
    if resultadoDasInstancias[jogada]:
        print('NAO', end=('\n'))
        
        
    else:
        print('SIM', end=('\n'))
        
    
           
        