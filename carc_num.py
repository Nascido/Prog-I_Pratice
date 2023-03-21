# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 21:56:44 2021

    Cálculo de fatorial

@author: Nascimento
"""
num = []
for i in range(5):
    x = int(input())
    num.append(x)

par   = 0
impar = 0

positivo = 0
negativo = 0

for x in num:
    if x % 2 == 0:
        par += 1
    
    else :
        impar += 1
        
    if x > 0:
        positivo += 1
        
    else:
        negativo += 1
        

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")
