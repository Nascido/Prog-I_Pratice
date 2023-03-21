# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:33:21 2021

    Saque de valor em Caixa Eletrônico

@author: Nascimento
"""
import numpy as np

num_cedulas = int(input())
caixa = []

for i in range(num_cedulas):
    cedula = []
    valor  = float(input())
    n      = int(input())
    
    cedula.append(valor)
    cedula.append(n)
        
    caixa.append(cedula)

saque = float(input())
retirada = np.zeros(num_cedulas, dtype=(np.int32))
i = 0

#Seleção das Cedulas
while saque > 0:
    i = 0
    for cedula in caixa[::-1]:
        quant  = saque//cedula[0]
        if cedula[0] <= saque and cedula[1] >= quant:
            saque -= cedula[0]*quant
            
            cedula[1]   -= 1 * quant
            retirada[i] += 1 * quant
            
        i += 1

for x in retirada[::-1]:
    print(x, end=(' '))