# -*- coding: utf-8 -*-
"""
Média mensal de chuvas

@author: Nascimento
"""

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

ano = cria_matriz(12, 31)
diasPorMes = []
for i in range(12):
    mes = [float(x) for x in input().split()]
    diasPorMes.append(len(mes))
    for j in range(len(mes)):
        ano[i][j] = mes[j]
        

somaMeses = [0]*12

for i in range(12):
    for j in range(31):
        somaMeses[i] += ano[i][j]
        
contador = 0
for soma in somaMeses:
    media = round(soma/diasPorMes[contador], 2)
    print(media, end=(' '))
    contador += 1