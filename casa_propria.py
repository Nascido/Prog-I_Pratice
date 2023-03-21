# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 16:24:34 2021

@author: Nascimento
"""

import turtle
import math

#Criando Operador
construtor = turtle.Turtle()

#Variavel de Medida
x = 100

#Desenhar o corpo da Casa
construtor.begin_fill()
construtor.fillcolor('blue')
for i in range(2):
    construtor.forward(2*x)
    construtor.left(90)
    construtor.forward(x)
    construtor.left(90)
construtor.end_fill()

#Desenhar a porta
construtor.begin_fill()
construtor.fillcolor('brown')
construtor.forward(x/3)
construtor.left(90)

construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3)
construtor.right(90)
construtor.forward(2*x/3)
construtor.left(90)
construtor.end_fill()

#Desenhar Janela
construtor.up()
construtor.forward(x/2)
construtor.left(90)
construtor.forward(x/3)
construtor.right(90)
construtor.down()

construtor.begin_fill()
construtor.fillcolor('cyan')
for i in range(4):
    construtor.forward(x/3)
    construtor.left(90)
construtor.end_fill()
    
#Desenhar Telhado
construtor.up()
construtor.left(90)
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3 + x/2)

construtor.begin_fill()
construtor.fillcolor('brown')
construtor.down()
construtor.left(135)
construtor.forward(x * math.sqrt(2))
construtor.left(90)
construtor.forward(x * math.sqrt(2))
construtor.end_fill()

#Tarefa Concluida
turtle.done()