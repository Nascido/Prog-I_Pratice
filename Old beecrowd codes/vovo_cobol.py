# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 12:29:46 2021

    Grace Hopper, a Vovó do Cobol

@author: Nascimento
"""
checkDeLetrasCobol = [False, False, False, False, False]
letrasCobol = ['c', 'o', 'b', 'o', 'l']
tamanhoDaPalavraCobol = len(letrasCobol)
resultadoDoTeste = []

while True:
    try:
        frase = input()
        frase = frase.lower()
        palavrasNaFrase = frase.split('-')
        contagemDeOs = 0
        for i in range(tamanhoDaPalavraCobol):
            for palavra in palavrasNaFrase:
                if palavra[0] == letrasCobol[i] or palavra[-1] == letrasCobol[i]: checkDeLetrasCobol[i] = True
                
        for palavra in palavrasNaFrase:   
           if palavra[0] == 'o' or palavra[-1] == 'o':
               contagemDeOs += 1
                    
        if contagemDeOs < 2: checkDeLetrasCobol[3] = False
        
        formaCobol = True
        for check in checkDeLetrasCobol:
            formaCobol = formaCobol and check
        
        if formaCobol:
            resultadoDoTeste.append('GRACE HOPPER')
            
        else:
            resultadoDoTeste.append('BUG')
        
        checkDeLetrasCobol = [False, False, False, False, False]
        
    except EOFError:
        
        for resultado in resultadoDoTeste:
            print(resultado)
            
        break
    
    
