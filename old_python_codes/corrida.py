# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:28:46 2021

    Corrida

@author: Nascimento
"""

carros, voltas = [int(x) for x in input().split()]


placar = []
for i in range(carros):
    tempo = [int(x) for x in input().split()]
    
    tempoTotal = 0
    
    for j in range(voltas):
        tempoTotal += tempo[j] 
    
    placar.append(tempoTotal)
    
maior     = min(placar)
primeiro = placar.index(maior) + 1
placar.pop(primeiro - 1)
placar.insert(primeiro - 1, 1000)


maior     = min(placar)
segundo = placar.index(maior) + 1
placar.pop(segundo - 1)
placar.insert(segundo - 1, 1000)

maior     = min(placar)
terceiro = placar.index(maior) + 1
placar.pop(terceiro - 1)
placar.insert(terceiro - 1, 1000)



print( primeiro )
print( segundo  )
print( terceiro ) 