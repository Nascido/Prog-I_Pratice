# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:54:10 2021
    
    Folha de Papel

@author: Nascimento
"""

c, p, f = [int(w) for w in input().split()]

if c*f <= p:
    print('S')
    
else:
    print('N')