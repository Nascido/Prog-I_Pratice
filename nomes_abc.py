# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:12:51 2021

    Juntar listas de nomes

@author: Nascimento
"""

n = int(input())
Nomes1 = []
for i in range(n):
    Nomes1.append(input())

n = int(input())
Nomes2 = []
for i in range(n):
    Nomes2.append(input())

Lista = Nomes1 + Nomes2

Lista.sort()


for nome in Lista:
    print(nome)