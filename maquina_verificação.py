# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 10:41:29 2021

    Máquina de Verificação Automatizada

@author: Nascimento
"""

conector1 = [int(x) for x in input().split()]
conector2 = [int(x) for x in input().split()]

teste = 'Y'
for i in range(len(conector1)):
    if conector1[i] == conector2[i]:
        teste = 'N'
        break

print(teste)