# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:10:55 2021

Verificar dígito verificador de um número

@author: Nascimento
"""

numero = input()

i = 2
soma = 0
for x in numero[-2::-1]:
    soma += int(x)*i
    i += 1
    
    
teste = 11 - (soma%11) 
if teste <= 9: result = teste == int(numero[-1])
else: result = 0 == int(numero[-1])

print()