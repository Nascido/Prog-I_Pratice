# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:04:42 2021

    Converter temperaturas

@author: Nascimento
"""

escalaEntrada = input()

valorEntrada   = float(input())

escalaSaida   = input()

if escalaEntrada == 'k':
    
    if escalaSaida == 'c':
        valorSaida = valorEntrada - 273.15
        
    elif escalaSaida == 'r':
        valorSaida = valorEntrada * 9/5
        
    else:
        valorSaida = (valorEntrada - 273.15)*1.8 + 32

elif escalaEntrada == 'c':
    
    if escalaSaida == 'k':
        valorSaida = valorEntrada + 273.15
        
    elif escalaSaida == 'r':
        valorSaida == (valorEntrada + 273.15)*9/5
       
        
    else:
        valorSaida = valorEntrada*1.8 + 32
        
elif escalaEntrada == 'r':
    
    if escalaSaida == 'c':
        valorSaida = valorEntrada*5/9 - 273.15
        
    elif escalaSaida == 'k':
        valorSaida = valorEntrada*5/9
        
    else:
        valorSaida = (valorEntrada - 459.67)
    
        
else:
    if escalaSaida == 'c':
        valorSaida = (valorEntrada - 32) / 1.8
        
    elif escalaSaida == 'r':
        valorSaida == valorEntrada + 459.67
        
    else:
        valorSaida = (valorEntrada - 32)*5/9 + 273.15
        
print(valorSaida)