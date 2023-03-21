# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:49:41 2021

    Número Aproximado de Primos

@author: Nascimento
"""

import numpy as np

n = int(input())

p = round(n/np.log(n),1)
m = round(1.25506*n/np.log(n),1)

print(f"{p} {m}")