# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 22:24:00 2021

    Cálculo de fatorial

@author: Nascimento
"""

n = int(input())
fat = 1
if n > 0:
    for x in range(1, n+1):
        fat *= x
        
print(fat)        