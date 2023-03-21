# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 22:15:20 2021

    Espécies de Madeira

@author: Nascimento
"""

casosTeste       = int(input())
leituraTeclado   = input()
contagemEspecies = []


while leituraTeclado == '' and casosTeste > 0:
    registroArvores = []
    leituraTeclado = input()
    
    while leituraTeclado != '':
        registroArvores.append(leituraTeclado)
        leituraTeclado = input()
        
    registroArvores.sort()
    quantidadeTotal = len(registroArvores)
    arvore = ''
    
    for i in range(quantidadeTotal):
        if arvore != registroArvores[i]: 
            arvore  = registroArvores[i]
            quantidadePorEspecie = registroArvores.count(arvore)
            porcentagem  = quantidadePorEspecie/quantidadeTotal
            
            levantamento = round(porcentagem * 1e+2, 4)
            contagemEspecies.append((arvore, levantamento))
        
    casosTeste -= 1
    if casosTeste > 0: contagemEspecies.append('proximo teste')
        
for dados in contagemEspecies:
    
    if dados == 'proximo teste': print('')
    
    else:
        print(f'{dados[0]} {dados:.4f}')
    