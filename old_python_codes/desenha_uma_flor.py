# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:23:24 2021

    Desenhar uma Flor

@author: Nascimento
"""
import turtle
def constroiPetala(petalas, angulo, raio, cor):
    '''
    Parameters
    ----------
    petalas : int
        Número de petalas.
    
    angulo : int
        Angulo da pétala.
        
    raio : float
        Seu tamanho.
        
    cor : string
        Sua cor por meio de strings.

    Returns
    -------
    None.
    '''
 
    for i in range(petalas):
        turtle.begin_fill()
        turtle.fillcolor(cor)
        turtle.circle(raio,angulo)
        turtle.left(180 - angulo)
        turtle.circle(raio,angulo)
        turtle.end_fill()
    

raio    = 60
cor     = 'pink' 
petalas = 7
angulo  = 77

#Cabo da Flor
turtle.left(90)
turtle.pensize(5)
turtle.forward(60)
turtle.pensize(1)


#Folha
turtle.right(90)
constroiPetala(1, 60, 100, 'green')
turtle.right(60+90)

#Cabo da Flor
turtle.pensize(5)
turtle.forward(120)
turtle.pensize(1)

#Pétalas
turtle.right(90)
constroiPetala(petalas, angulo, raio, cor)
turtle.right(60+90)

#botão
turtle.dot(20, 'yellow')


turtle.done()