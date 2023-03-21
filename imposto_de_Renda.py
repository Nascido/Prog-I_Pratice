# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 21:29:19 2021

    Cálculo de Imposto de Renda
    
IRRF = (Salário Bruto - DescontoPorDependentes - INSS) * Alíquota – Dedução

INSS
--------------------------------------------------------------------------
 salário bruto até R$ 720,00 tem um valor de 7.65% sobre o salário bruto;
 salário bruto até R$ 1.200,00 tem um valor de 9% sobre o salário bruto;
 salário bruto até R$ 2.400,00 tem um valor de 11% sobre o salário bruto;
 salário bruto acima de R$ 2.400,00 tem um valor de 11% sobre R$ 2.400,00;
--------------------------------------------------------------------------
 
desconto de R$ 137,99 por dependente

@author: Nascimento
"""

salario    = float(input())
dependente = int(input())


#Dedução e Alíquota
if salario <= 1372.81:
    aliquota = 0
    dedução  = 0
    
elif salario <= 2743.25:
    aliquota = 0.15
    dedução  = 205.92

else:
    aliquota = 0.275
    dedução  = 548.82
    
    
    
#INSS
if salario <= 720.00:
    INSS = salario * 0.0765

elif salario <= 1200.00:
    INSS = salario * 0.09
    
elif salario <= 2400.00:
    INSS = salario * 0.11
    
else:
    INSS = 2400.00 * 0.11
    

#Cálculo do imposto
IRRF = (salario - dependente*137.99 - INSS) * aliquota - dedução

if IRRF < 0: IRRF = 0.0

print(round(IRRF, 2))






