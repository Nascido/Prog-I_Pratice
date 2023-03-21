# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:31:25 2021

    Errrou!

@author: Nascimento
"""

casosTeste = int(input())
ErrousGuardados = []

for i in range(casosTeste):
    Errou = ['E', 'o', 'u', '!']
    expressão = input()
    
    parteEsquerda, parteDireita = expressão.split('=')
    
    if  parteEsquerda.count('+') > 0:
        operação = '+'
        
    elif parteEsquerda.count('-') > 0:
        operação = '-'
    
    else:
        operação = 'x'
        
    numeroA, numeroB = parteEsquerda.split(operação)
    
    resposta = int(parteDireita)
    numeroA  = int(numeroA) 
    numeroB  = int(numeroB)
    
    if  parteEsquerda.count('+') > 0:
        gabarito = numeroA + numeroB
        
    
    elif parteEsquerda.count('-') > 0:
        gabarito = numeroA - numeroB
        
        
    else:
        gabarito = numeroA * numeroB
        
    
    Errou.insert( 1, 'r' * abs(gabarito - resposta))
    
    frase = ''
    
    for letra in Errou:
        frase += letra
    
    ErrousGuardados.append(frase)
    
    
for errou in ErrousGuardados:
    print(errou)

