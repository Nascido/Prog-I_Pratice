# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 19:13:09 2021

    Sequências Crescentes

@author: Nascimento
"""

x = 1
seq = []
while x != 0:
    x = int(input())
    seq.append(x)

for x in seq:
    for i in range(1 , x+1):
        print(i)
        
        if i < x: print(' ', end = '')
        
        else: print('')
