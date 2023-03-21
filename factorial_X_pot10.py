# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:51:00 2021

    Menor valor que satisfaz a desigualdade

@author: Nascimento
"""

from math import factorial

n = 1
while factorial(n) <= n**(10):
    n += 1

print(n)