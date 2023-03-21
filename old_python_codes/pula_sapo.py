# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 11:24:44 2021

    Pula Sapo

@author: Nascimento
"""

limite, qtdade = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]


falhou = False
for i in range(qtdade - 1):
    if alturas[i+1]-alturas[i] > limite:
        falhou = True
            
            
if falhou:
    print('GAME OVER')

else:
    print('YOU WIN')