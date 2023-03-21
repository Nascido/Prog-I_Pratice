# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 11:05:24 2021

    Cartas

@author: Nascimento
"""
import numpy as np

sequencia = [int(x) for x in input().split()]

teste = 'N'


verificação  = np.copy(sequencia)

sequencia.sort()
crescente    = np.copy(sequencia)

sequencia.sort(reverse=True)
descrescente = np.copy(sequencia)


if np.array_equal(verificação, crescente):
    teste = 'C'
    
elif np.array_equal(verificação, descrescente):
    teste = 'D'
    
    
print(teste)