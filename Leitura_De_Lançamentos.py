# -*- coding: utf-8 -*-


lançamentos = [3, 5, 4, 3, 3, 1, 3, 1, 1, 1, 1, 2, 5, 1, 6]


def Leitura_De_Lançamentos(lançamentos):

    facesRepetidas = []
    
    faceAnterior = -1
    sequenciasRepetidas = 0
    
    for i in range(len(lançamentos)):
        
        face = lançamentos[i]
        
        if face == faceAnterior:
            sequenciasRepetidas += 1
            
            if i - 2 >= 0:
                if lançamentos[i-2] == face:
                    sequenciasRepetidas -= 1
         
        repetições = lançamentos.count(face)       
        if repetições > 1:
            facesRepetidas.append((repetições, face))
            
            
        faceAnterior = face
        
    facesRepetidas.sort()
    
    faceQueMaisSeRepetiu = facesRepetidas[-1]
    
    return sequenciasRepetidas, faceQueMaisSeRepetiu[-1]