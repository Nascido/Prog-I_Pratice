# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:43:46 2021

    Garçon

@author: Nascimento
"""

N = int(input())

quebrados = 0
while N > 0:
    latas, copos = [int(w) for w in input().split()]
    if latas > copos:
        quebrados += copos
    
    N -= 1
    
print(quebrados)
    