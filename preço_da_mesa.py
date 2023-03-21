# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:53:27 2021

    Preço de uma mesa

@author: Nascimento
"""
 







comprimento = 1.2
largura     = 1
gavetas     = 2
madeira     = 'canela'

area  = comprimento*largura
preço = 0

    

if area > 2: preço += 50.00

if madeira == 'mogno': preço += 150.00
elif madeira == 'carvalho': preço += 125.00

preço += gavetas*30 + area*100

if preço < 200: preço = 200.00
 
print(round(preço, 2))