# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:34:23 2021

    Contar número de Marias

@author: Nascimento
"""

n = int(input())
cont = 0
for i in range(n):
    coleta = input()
    nome   = coleta.replace('Mariana', '')
    if 'Maria ' in nome or ' Maria' in nome: cont += 1
print(cont)