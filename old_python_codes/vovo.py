# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:43:07 2021

    Saldo do Vovô

@author: Nascimento
"""

dias, saldo = [int(w) for w in input().split()]

menor = saldo

for i in range(dias):
    mov    = int(input())
    saldo += mov
    
    if menor >= saldo:
        menor = saldo
        
print(menor)