# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:45:10 2021

    Calcular prêmio de seguro

@author: Nascimento
"""

valorVeículo  = float(input())
classe        = input()
procedencia   = input()
idadeSegurado = int(input())


#Descontos por Classe
if classe == 'A':
    desconto = 0.3

elif classe == 'B':
    desconto = 0.2

elif classe == 'C':
    desconto = 0.1

elif classe == 'D':
    desconto = 0.05
    
else:
    desconto = 0
    
#Descontos por Idade
if idadeSegurado >= 24:
    desconto += 0.1
    
#Custo por Procedência
if procedencia == 'nacional':
    percentual = 0.1

else:
    percentual = 0.15
    
#Cálculo Prêmio
premio = valorVeículo*percentual *(1 - desconto)

print(round(premio, 2))









