# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:49:10 2021

    Juros Compostos

@author: Nascimento
"""

capital = float(input())
meses   = int  (input())
taxa    = float(input())/100

montante = round (capital*((1 + taxa))**meses, 2)

print(montante)