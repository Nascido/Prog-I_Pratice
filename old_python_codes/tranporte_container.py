# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 10:45:39 2021

    Transporte de Containers

@author: Nascimento
"""

a, b, c = [int(w) for w in input().split()]
x, y, z = [int(w) for w in input().split()]

QuantidadeX = int(x/a)
QuantidadeY = int(y/b)
QuantidadeZ = int(z/c)

Quantidade_Máxima = QuantidadeX*QuantidadeY*QuantidadeZ

print(Quantidade_Máxima)

