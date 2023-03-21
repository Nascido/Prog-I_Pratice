# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:06:59 2021

    Abreviar o nome de uma pessoa

@author: Nascimento
"""

nome = input()
abreviação = nome.split()

i = 0
for x in abreviação:
    if len(x) > 3 and i > 0 and i < len(abreviação)-1:
        abreviação[i] = x[0] + '.'
        
        
    i += 1
    
for x in abreviação:
    print(x, end=(' '))