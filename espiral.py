# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:29:45 2021

    Espiral

@author: Nascimento
"""

import turtle

pincel = turtle.Turtle()
r = 20
for i in range(0,100,1):
    r += r*1.6181
    pincel.forward(r)
    pincel.left(92)
    
turtle.done()