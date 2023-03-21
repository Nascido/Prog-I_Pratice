# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:51:49 2021

    Decifra

@author: Nascimento
"""

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

cifra    = input()

mensagem = input()

cripto = {k: v for k, v in zip(cifra, alfabeto)}


for letra in mensagem:
    print(cripto[letra], end=(''))