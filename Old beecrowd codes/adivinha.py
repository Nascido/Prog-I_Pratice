# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 10:07:03 2021

    Adivinha

@author: Nascimento
"""

testes = int(input())
resultado = []

for i in range(testes):
    alunos, sorteio = input().split()
    alunos  = int(alunos)
    sorteio = int(sorteio)
    
    chutes = [int(x) for x in input().split()]
    chutes = chutes[:alunos]
    
    diferença = []
    for chute in chutes:
        diferença.append(abs(chute - sorteio))
        
    
    resultado.append(diferença.index(min(diferença)) + 1)
    
    
for x in resultado:
    print(x)