# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:22:52 2021

    Relógio

@author: Nascimento
"""

import turtle


pincel = turtle.Turtle()

#Circuferência externa
pincel.circle(100)

#Minutos
pincel.up()
pincel.left(90)
pincel.forward(10)
pincel.right(90)

for i in range(12):
    pincel.dot()
    pincel.circle(90, 30)
    
#ponteiro segundos
pincel.left(90)
pincel.forward(90)
pincel.left(25)
pincel.down()
pincel.color('red')
pincel.forward(90)
    
pincel.right(180)
pincel.forward(90)

#ponteiro minutos
pincel.right(25)
pincel.color('black')
pincel.width(3)
pincel.forward(80)

pincel.right(180)
pincel.forward(80)

#ponteiro horas
pincel.left(45)
pincel.width(5)
pincel.forward(70)







turtle.done()