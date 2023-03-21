# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:27:37 2021

    Número de acertos numa prova

@author: Nascimento
"""

gabarito = input()
resposta = input()

if len(resposta) == len(gabarito):

    i       = 0
    acertos = 0
    for x in gabarito:
        if x == resposta[i]: acertos += 1
        i += 1
        
    print(acertos)

else: print('erro')