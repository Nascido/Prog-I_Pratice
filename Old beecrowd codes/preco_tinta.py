# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:04:04 2021

    Preço da Tinta

@author: Nascimento
"""

area = int(input())

#valores
TintaNecessaria = area/18
latas = max(round(TintaNecessaria/3.6), 1)
preçoTotal = latas * 25

#saída
print('- área de cobertura:', area)
print('- número de galões:', latas)
print('- valor a ser pago: R$ {:.2f}'.format(preçoTotal))