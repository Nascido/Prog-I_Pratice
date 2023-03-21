# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:16:22 2021

    Media Aprovação

@author: Nascimento
"""

p1 = float(input())
p2 = float(input())
p3 = float(input())

peso1 = float(input())
peso2 = float(input())
peso3 = float(input())

media = (p1*peso1 + p2*peso2 + p3*peso3)/(peso1 + peso2 + peso3)

print(media >= 6)