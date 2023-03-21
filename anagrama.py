# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:49:05 2021

    Anagrama

@author: Nascimento
"""

palavra1 = input()
palavra2 = input()

result = True

palavra1 = palavra1.replace(' ', '')
palavra2 = palavra2.replace(' ', '')
palavra1 = palavra1.replace('-', '')
palavra2 = palavra2.replace('-', '')
palavra1 = palavra1.replace(',', '')
palavra2 = palavra2.replace(',', '')

if len(palavra1) != len(palavra2):
    result = False
    
if palavra1 == palavra2:
    result = False
    
n = len(palavra1)

for i in range(n):
    if not result: break
    result  = False
    vezes   = palavra1.count(palavra1[i])
    contado = 0
    for j in range(n):
        if palavra1[i] == palavra2[j]:
            result   = result or True
            contado += 1
    if result:
        if contado != vezes:
            result = False

print(result)