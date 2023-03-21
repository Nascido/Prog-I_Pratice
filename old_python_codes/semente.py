# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:12:17 2021

    Semente

@author: Nascimento
"""

tamanhoDaFita, numeroDeGotas = [int(x) for x in input().split()]
posiçãoGotas = [int(x) for x in input().split()]
posiçãoGotas = posiçãoGotas[:numeroDeGotas]

fita = []
for i in range(tamanhoDaFita):
    fita.append('')
    
for posição in posiçãoGotas:
    fita[posição-1] = 0
    


contadorDeDias = 0
while fita.count('') > 0 :
    
    for i in range(tamanhoDaFita):
        if fita[i] == 0:
            if i - 1 >= 0:
               if fita[i-1] == '':
                   fita[i-1] = 'o'
                   
            if i + 1 < tamanhoDaFita: 
                if fita[i+1] == '':
                    fita[i+1] = 'o'
            
    for i in range(tamanhoDaFita):
        if fita[i] == 'o':
            fita[i] = 0
            
    contadorDeDias += 1
    

print(contadorDeDias)