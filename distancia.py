# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 16:55:50 2021

    Distância entre Dois Pontos

@author: Nascimento
"""

import math

xi, yi = [float(w) for w in input().split()]
xf, yf = [float(w) for w in input().split()]

distancia = math.sqrt((xf - xi)**2 + (yf - yi)**2)

print(round(distancia, 4))