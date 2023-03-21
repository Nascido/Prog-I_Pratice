# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:41:19 2021

    Palíndromo

@author: Nascimento
"""

frase = input()
frase = frase.replace(' ', '')

print(frase == frase[::-1])