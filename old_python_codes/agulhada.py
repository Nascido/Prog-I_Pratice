# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:32:27 2021

    Calouros doadores de sangue

@author: Nascimento
"""

n = int(input())
calouros = []
for i in range(n):
    calouros.append(input())

n = int(input())
geral = []
for i in range(n):
    geral.append(input())

contador = 0
for nome in calouros:
    if nome in geral:
        contador += 1
        
print(contador/len(calouros))