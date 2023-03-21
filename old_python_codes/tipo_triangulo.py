# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:10:04 2021

    Tipo de Triângulo

@author: Nascimento
"""

ladoA = int(input())
ladoB = int(input())
ladoC = int(input())


if ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
    print('escaleno')

elif ladoA == ladoB and ladoA == ladoC and ladoB == ladoC:
    print('equilátero')
    
else:
    print('isósceles')
    