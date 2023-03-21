# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:40:23 2021

@author: Nascimento
"""

salarioBruto = float(input())

if salarioBruto <= 720.00:
    percentual = 0.0765
    
elif salarioBruto <= 1200.00:
    percentual = 0.09

elif salarioBruto <= 2400.00:
    percentual = 0.11
    
else:
    salarioBruto = 2400.00
    percentual   = 0.11
    
print(salarioBruto*percentual)