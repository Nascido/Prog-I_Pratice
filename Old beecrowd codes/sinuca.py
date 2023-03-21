# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 12:01:11 2021

    Sinuca

@author: Nascimento
"""

bolasPorFileira = int(input())
coresDasBolasPorFileira = [int(x) for x in input().split()]


while bolasPorFileira > 1:
    proximaFileira = []
    for i in range(bolasPorFileira - 1):
        proximaFileira.append(coresDasBolasPorFileira[i] * coresDasBolasPorFileira[i+1])
        
    coresDasBolasPorFileira = proximaFileira
    bolasPorFileira = len(coresDasBolasPorFileira)
    
    
deNumeroParaCor = {-1:'branca', 1:'preta'}
print(deNumeroParaCor[coresDasBolasPorFileira[0]])