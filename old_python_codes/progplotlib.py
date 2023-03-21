# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:17:24 2021

    Biblioteca de Programação OO

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
    