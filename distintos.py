# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:18:25 2021

    Calcular número de valores distintos

@author: Nascimento
"""



n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

distintos = 4


if n1 == n2: distintos -= 1
if n1 == n3: distintos -= 1
if n1 == n4: distintos -= 1

if n2 == n3 and n2 != n1: distintos -= 1
if n2 == n4 and n2 != n1: distintos -= 1

if n3 == n4 and n3 != n1 and n3 != n2  : distintos -= 1

print(distintos)


