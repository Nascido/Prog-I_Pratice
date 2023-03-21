# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:14:19 2021

    Cara ou Coroa

@author: Nascimento
"""

n = int(input())
geral = []
vezes = 0
while n != 0:
    pontos = [0,0]
    jogada = input()
    for i in jogada:
        if i == '0': pontos[0] += 1
        if i == '1': pontos[1] += 1
    
    geral.append(pontos)
    vezes += 1
    n = int(input())
    
for i in range(vezes):
    pontos = geral[i]
    print(f'Mary won {pontos[0]} times and John won {pontos[1]} times')