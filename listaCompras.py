# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:40:14 2021

    Lista de Compras

@author: Nascimento
"""

n = int(input())
lista = []

for i in range(n):
    compras = [str(x) for x in input().split()]
    
    for produto in compras:
        i = compras.count(produto)
        if i > 1:
            for x in range(i-1):
                posicao = compras.index(produto)
                compras.pop(posicao)

    compras.sort()
    
    lista.append(compras)
    lista.append('_')

for produto in lista:
    if produto == '_': print('\n')
    else: print(produto)