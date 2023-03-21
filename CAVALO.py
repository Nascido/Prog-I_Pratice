# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:57:14 2021

    Xadrez: Cavalo

@author: Nascimento
"""

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

confirmação = False

if abs(x1 - x2) == 1:
    if  abs(y1 - y2) == 2:
        confirmação = not confirmação
        
if abs(x1 - x2) == 2:
    if abs(y1 - y2) == 1:
        confirmação = not confirmação
    
print(confirmação)