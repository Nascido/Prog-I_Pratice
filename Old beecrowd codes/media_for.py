# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:03:44 2021

    Média dos valores

@author: Nascimento
"""
tamanho = int(input())
numeros = []
for i in range(tamanho):
    numeros.append(float(input()))
    
print(sum(numeros)/tamanho)