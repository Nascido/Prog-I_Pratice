# -*- coding: utf-8 -*-

def operacoes_Algebricas(codigo, a, b, c):

    
    if codigo == 1:
        areaDoTrapezio = (a + b)*c/2
        
        return areaDoTrapezio
        
    elif codigo == 2:
        
        MultiplicaçãoAxB = a * b
        
        MultiplicaçãoBxA = b * a
        
        MultiplicaçãoCxA = c * a
        
        
        return (MultiplicaçãoAxB, a, b), (MultiplicaçãoBxA, b, a), (MultiplicaçãoCxA, c, a)
        
    elif codigo == 3:
        
        mediaAritimetica = (a + b + c)/3
        
        return (mediaAritimetica, a, b, c)
    
    else:
        
        somaInteiros = 0    
        for i in range(a, b+1, c):
            
            somaInteiros += i
            
        return somaInteiros
            