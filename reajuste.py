# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:21:17 2021

    Reajuste de salário

@author: Nascimento
"""

salario       = float(input())
salarioMinimo = float(input())

nMinimos = salario/salarioMinimo

if nMinimos < 3:
    ajuste = salario*1.2
    
elif nMinimos <= 5:
    ajuste = salario*1.15
    
else:
    ajuste = salario*1.1
    
if (ajuste - salario) < 1.5*salarioMinimo:
    ajuste = salario + 1.5*salarioMinimo

elif (ajuste - salario) > 20*salarioMinimo:
    ajuste = salario + 1.5*salarioMinimo
    
print(ajuste)