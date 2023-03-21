# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:23:29 2021

    Múltiplos de n

@author: Nascimento
"""

n = int(input())
m = int(input())

for i in range(1, m + 1):
    if i % n == 0:
        print(i, end=' ')
        
