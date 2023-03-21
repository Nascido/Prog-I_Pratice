# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:11:32 2021

    Cálculo das Raízes de uma Função Quadrádica

@author: Nascimento
"""

a = int(input())
b = int(input())
c = int(input())
    
import math

#Bhaskara

delta = b**2 - 4*a*c

if delta >= 0:
    print((-b + math.sqrt(delta))/(2*a), (-b - math.sqrt(delta))/(2*a))

