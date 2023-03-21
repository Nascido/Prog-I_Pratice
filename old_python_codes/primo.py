# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:31:26 2021

@author: Nascimento
"""

n = int(input())
primo = True
for divisor in range(2, n):
    if n % divisor == 0:
        primo = False
        break
   
        
print(primo and n != 1)