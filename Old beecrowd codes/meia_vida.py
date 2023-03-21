# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 23:30:52 2021

    Massa radioativa

@author: Nascimento
"""

massa = int(input())

tempo = 0
while massa >= 0.5:
    massa /= 2
    tempo += 50
    
print(tempo)