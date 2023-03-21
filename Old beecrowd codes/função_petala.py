# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:31:20 2021

@author: Nascimento
"""

import turtle

def petala(posx, posy, raio, angulo,cor):

    """ Desenho de uma pétala."""
    
    # Atributos
    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()
    turtle.fillcolor(cor)
    turtle.begin_fill()
    
    # Desenha
    turtle.circle(raio,angulo)
    turtle.setheading(turtle.heading() + 180 - angulo)
    turtle.circle(raio,angulo)
    turtle.setheading(turtle.heading() + 180 - angulo)
    
    # Termina
    turtle.end_fill()
    turtle.hideturtle()
    
    turtle.done()