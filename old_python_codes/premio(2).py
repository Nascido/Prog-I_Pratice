# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 18:56:35 2021

    Prêmio de Seguro (2)

Sexo/idade -/-	Até 24 anos	/ Entre 25 e 33 anos / Mais de 33 anos
M	              0%	           10%                20%
F	              5%	           20%	              35%

@author: Nascimento
"""

valorVeiculo = 10000

sexo  = 'M'
idade = 24

if sexo == 'M':
    if idade <= 24:
        desconto = 0
    
    elif idade <= 33:
        desconto = 0.1
        
    else:
        desconto = 0.2
        
else:
    if idade <= 24:
        desconto = 0.05
    
    elif idade <= 33:
        desconto = 0.2
        
    else:
        desconto = 0.35
        
premio = valorVeiculo*0.1 * (1 - desconto)