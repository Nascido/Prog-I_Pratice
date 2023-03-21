# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 15:21:27 2021

    Condição de Existência de um Triângulo

@author: Nascimento
"""

ladoA = float(input())
ladoB = float(input())
ladoC = float(input())


condiçãoA = abs(ladoB - ladoC) < ladoA < ladoB + ladoC
condiçãoB = abs(ladoA - ladoC) < ladoB < ladoA + ladoC
condiçãoC = abs(ladoA - ladoB) < ladoC < ladoA + ladoB

ser_um_triangulo = condiçãoA and condiçãoB and condiçãoC

print(ser_um_triangulo)

