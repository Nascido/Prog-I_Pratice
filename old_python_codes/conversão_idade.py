# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 15:46:24 2021

    Conversão Idade

@author: Nascimento
"""

idadeDias = int(input())


anos   = int(idadeDias/365)
meses  = int((idadeDias % 365)/30)
dias   = idadeDias % 365 - 30*meses


print(f"{anos} ano(s)")
print(f"{meses} mes(es")
print(f"{dias} dia(s)")