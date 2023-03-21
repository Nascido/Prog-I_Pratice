# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:47:31 2021

    Handebol

@author: Nascimento
"""

jogadores, partidas = [int(x) for x in input().split()]

jogadoresQueMarcaramEmTodas = 0
for i in range(jogadores):
    golsDoJogador = [int(x) for x in input().split()]
    
    for j in range(partidas):
        if golsDoJogador[j] > 0: acerto = True
        
        else:
            acerto = False
            break

    if acerto: jogadoresQueMarcaramEmTodas += 1
    
print(jogadoresQueMarcaramEmTodas)