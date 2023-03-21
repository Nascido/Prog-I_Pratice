# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:46:29 2021

    Calcular o MDC (máximo divisor comum) entre dois números

@author: Nascimento
"""

n1 = int(input())
n2 = int(input())

menor = min(n1, n2)
divisor = 2
mdc = 1

while divisor <= menor:
    if n1 % divisor == 0 and n2 % divisor == 0:
        mdc = divisor
        
    divisor += 1
    
print(mdc)