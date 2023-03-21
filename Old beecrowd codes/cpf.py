# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 22:13:05 2021

    Validar CPF

@author: Nascimento
"""

cpf = input()

cpf = cpf.replace('-', '')
cpf = cpf.replace('.', '')

j = True
for x in cpf:
    for i in range(11):
        j = j and x == cpf[i]
    

verif1 = False
verif2 = False
i = 2
soma = 0
if len(cpf) == 11 and not j:
    for x in cpf[-3::-1]:
        soma += int(x)*i
        i += 1
        
    teste = (soma*10)%11
    if teste >= 10: teste = 0
    
    if teste == int(cpf[-2]):
        verif1 = True
    
    i = 2
    soma = 0
    for x in cpf[-2::-1]:
        soma += int(x)*i
        i += 1
    
    teste = (soma*10)%11
    if teste >= 10: teste = 0
    if teste == int(cpf[-1]):
        verif2 = True
    
    print(verif1 and verif2)

else:
    print(False)