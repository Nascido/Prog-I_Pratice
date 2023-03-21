# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:06:37 2021

    Palhaço
    
@author: Nascimento
"""

import turtle

#Olhos
turtle.up()
turtle.forward(25)
turtle.dot(50,'black')
turtle.right(180)
turtle.forward(50)
turtle.dot(50,'black')

#Maquiagem
turtle.right(180)
turtle.forward(25)
turtle.right(90)
turtle.pencolor('blue')
turtle.down()

for i in [50, 75, 100]:
    turtle.circle(i)
    
turtle.right(180)
for i in [50, 75, 100]:
    turtle.circle(i)
    
#Boca
turtle.right(270)
turtle.up()
turtle.forward(180)
turtle.down()
turtle.circle(180, extent=None, steps=None)

#Nariz
turtle.right(180)
turtle.up()
turtle.forward(130)
turtle.down()
turtle.pencolor('red')
for i in range (25):
    turtle.forward(100)
    turtle.left(179)


turtle.done()