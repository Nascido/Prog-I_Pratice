# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 15:46:24 2021

    Conversão de Tempo

@author: Nascimento
"""

tempoSegundos = 500*60*5


horas    = int(tempoSegundos/3600)
minutos  = int(tempoSegundos/60) - horas*60
segundos = tempoSegundos % 60


print(f"{horas}:{minutos}:{segundos}")