# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:54:15 2021

    Perguntas mais Frequentes

@author: Nascimento
"""

n    = 1
freq = 1
n, freq   = [int(x) for x in input().split()]
listaFreq = []

while n != 0 and freq != 0:
    listaPerguntas = []
    cont = 0
    duvidas = [int(x) for x in input().split()]
    
    for pergunta in duvidas:
        if duvidas.count(pergunta) >= freq and not pergunta in listaPerguntas:
            listaPerguntas.append(pergunta)
            
    listaFreq.append(len(listaPerguntas))
    
    n, freq = [int(x) for x in input().split()]
    
for i in listaPerguntas:
    print(i)