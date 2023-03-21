# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:09:48 2021

Revisão de Contrato

@author: Nascimento
"""

digitoProblema, valorOriginal  = [str(x) for x in input().split()]


valoresFalsos = []

while digitoProblema != '0' and valorOriginal != '0':
    
    valorAdulterado = valorOriginal.replace(digitoProblema, '')
    
    if valorAdulterado == '':
        valorAdulterado = '0'
        
    valoresFalsos.append(int(valorAdulterado))
    
    digitoProblema, valorOriginal  = [str(x) for x in input().split()]
    
for valor in valoresFalsos:
    print(valor)
    
    
         