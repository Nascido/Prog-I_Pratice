# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:53:20 2021

    Contar primos

@author: Nascimento
"""

inicio = int(input())
fim    = int(input())

sec = []
for n in range(inicio, fim + 1):

    primo = True
    for divisor in range(2, n):
        if n % divisor == 0:
            primo = False
            break    
    
    sec.append(primo and n != 1)
    
print(sum(sec))