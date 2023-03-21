# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:32:51 2021

    Flowers Flourish from France

@author: Nascimento
"""

frase = input()
tautograma = []

while frase[0] != '*':
    teste = []
    frase = frase.lower()
    tauto = frase[0]
    
    palavras = frase.split(' ')
    
    for x in palavras:
        teste.append(x[0] == tauto)
        
    if sum(teste) == len(palavras):
        tautograma.append('Y')
    
    else:
        tautograma.append('N')
        
    frase = input()
    
for x in tautograma:
    print(x)