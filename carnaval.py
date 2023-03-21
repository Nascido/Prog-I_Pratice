# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:55:00 2021

    Carnaval

@author: Nascimento
"""

notas = [float(x) for x in input().split()]

notas.sort()

notas.pop()
notas.pop(0)

print(round(sum(notas), 1))

