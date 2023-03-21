# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:08:57 2021

    Cálculo Pedágio

@author: Nascimento
"""

L, D = [float(w) for w in input().split()]
K, P = [float(w) for w in input().split()]

pedágios = int( L/D )

custoKm       = L * K
custoPedágios = pedágios * P

custoTotal    = custoKm + custoPedágios

print(int(custoTotal))