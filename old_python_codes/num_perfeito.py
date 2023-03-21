# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:56:26 2021

    Número Perfeito

@author: Nascimento
"""
n = int(input())

perfeitos = []
num = []
for j in range(n):
    num.append(int(input()))
    
    
for x in num:
    soma = 0
    for i in range(1, x):
        if x%i == 0: soma += i
    
    if soma == x: perfeitos.append(True)
    else: perfeitos.append(False)
    
contador = 0
for i in perfeitos:
    if i : print(f'{num[contador]} eh perfeito')
    else : print(f'{num[contador]} nao eh perfeito')
        
    contador += 1