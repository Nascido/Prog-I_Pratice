# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:55:05 2021

    Detectando Colisões

@author: Nascimento
"""

Ax0, Ay0, Ax1, Ay1 = [int(w) for w in input().split()]

Bx0, By0, Bx1, By1 = [int(w) for w in input().split()]

condição = True


if Bx0 < Ax0:
   if Bx1 < Ax0: condição = False

elif Bx1 > Ax1:
    if Bx0 > Ax1: condição = False
        
    
if By0 < Ay0:
    if By1 < Ay0: condição = False

elif By1 > Ay1:
    if By0 > Ax1: condição = False
    
print(int(condição))
