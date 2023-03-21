# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:20:44 2021

    Custo de locação de um veículo

@author: Nascimento
"""

dias = int(input())
km   = float(input())


if km > 60*dias :
    preço = 45.0*dias + (km - 60*dias)*0.5

else:
    preço = 45.0*dias
    
print(round(preço, 2))
    