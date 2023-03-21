# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:59:56 2021

    Descriptograr um texto

@author: Nascimento
"""

alfabeto = input()
cifra    = input()

mensagem = input()

cripto = {k: v for k, v in zip(cifra, alfabeto)}

cripto[' '] = ' '
cripto['!'] = '!'
cripto[','] = ','
cripto['.'] = '.'

for letra in mensagem:
    print(cripto[letra], end=(''))