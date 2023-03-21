# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:34:41 2021

    Obter conceito dadas três notas

@author: Nascimento
"""

nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

media = (nota1 + nota2 + nota3)/3

if  media >= 9.0:
    print('Ótimo')
    
elif media >= 7.5:
    print('Bom')
    
elif media >= 6.0:
    print('Satisfatório')

else:
    print('Insuficiente')