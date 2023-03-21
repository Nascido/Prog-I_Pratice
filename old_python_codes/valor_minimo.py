# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:57:18 2021

    Menor valor de uma sequência

@author: Nascimento
"""

tamanho = int(input())

lista = []
for n in range(tamanho):
    lista.append(int(input()))
    
print(min(lista))