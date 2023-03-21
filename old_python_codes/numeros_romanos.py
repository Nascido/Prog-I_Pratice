# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 09:22:59 2021

    Converter um número romano para decimal

@author: Nascimento
"""

valores_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

numero_romano = input()

decimal = 0

for i in range(len(numero_romano)-1):
    dr0 = numero_romano[i]
    dr1 = numero_romano[i+1]
    
    if valores_romanos[dr0] >= valores_romanos[dr1]:
        decimal += valores_romanos[dr0]
        
    else:
        decimal -= valores_romanos[dr0]
        
decimal += valores_romanos[numero_romano[-1]]


print(decimal)