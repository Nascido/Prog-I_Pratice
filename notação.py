# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:11:52 2021

    Notação Científica

@author: Nascimento
"""

n = float(input())

pot = 0
sinal = ''
decimalpot = ''
while abs(n) < 1.0:
    n   *= 10
    pot -= 1
    
while abs(n) > 10.0:
    n   /= 10
    pot += 1
    
if n >= 0: 
    sinal = '+'

else:
    sinal = '-'


if pot >= 0: 
    sinalpot = '+'
    
else:
    sinalpot = '-'

if abs(pot) < 10: decimalpot = '0'

mantissa = str(round(abs(n) , 4)) + '0000'

print(f'{sinal}{mantissa[0:6]}E{sinalpot}{decimalpot}{abs(pot)}')
    
