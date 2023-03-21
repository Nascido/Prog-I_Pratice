# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:36:26 2021

    Sequência de Fibonacci

@author: Nascimento
"""

n = int(input())

a0 = 0
a1 = 1
aN = 1
for i in range(n-1):
    aN = a0 + a1
    a0 = a1
    a1 = aN
    
print(aN)