# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:06:56 2021

    Converter um número decimal em binário

@author: Nascimento
"""

n = int(input())
binario = []

while n >= 0:
    binario.append(n % 2)
    n //= 2
    
for i in binario[::-1]:
    print(i, end = '')