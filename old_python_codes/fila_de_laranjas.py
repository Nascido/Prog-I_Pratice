# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:37:16 2021

    Fila de Laranjas

@author: Nascimento
"""

import turtle

pincel = turtle.Turtle()


pincel.up()

for r in range(10, 90, 10):
    pincel.left(90)
    pincel.forward(r/2)
    pincel.down()
    pincel.dot(r,'orange')
    pincel.up()
    pincel.right(180)
    pincel.forward(r/2)
    pincel.left(90)
    pincel.forward(r+5)


turtle.done()