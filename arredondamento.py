# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:54:37 2021

    Arredondamento UFSC

@author: Nascimento
"""

nota   = 6.5
fração = nota - int(nota)

if fração >= 0.25 and fração < 0.75:
    fração = 0.5
    nota = round(nota) + fração
    
else:
   nota = round(nota)
    
print(nota)