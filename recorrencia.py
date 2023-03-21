# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:40:10 2021


    Obter a letra que mais aparece


@author: Nascimento
"""

frase = input()

frase = frase.lower()
frase = frase.replace(' ', '')

maior = 0
for letra in frase:
    if frase.count(letra) >= maior:
        maior    = frase.count(letra)
        repetida = letra 
        
        
print(repetida)