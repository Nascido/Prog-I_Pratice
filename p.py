# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:39:07 2021

    Língua do P

@author: Nascimento
"""

codigo = input()
mensagem = []

i = 1
while i < len(codigo):
    
    mensagem.append(codigo[i])
    
    if i < len(codigo)-1:
        if codigo[i + 1] == ' ' : 
            i += 3
            mensagem.append(' ')
        
        else:
            i += 2
    else:
        i += 2
    
print(''.join(mensagem))