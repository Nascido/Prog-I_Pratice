# -*- coding: utf-8 -*-
"""
Choque de horário

@author: Nascimento
"""

quantidadeDeMaterias = int(input())

def cria_matriz(n_linhas, n_colunas, valor_inicial = 0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

TabelaDeHorarios = cria_matriz(quantidadeDeMaterias, 7, valor_inicial='')

for i in range(quantidadeDeMaterias):
    DisciplinaEHorarios = [str(x) for x in input().split()]
    for j in range(len(DisciplinaEHorarios)):
        TabelaDeHorarios[i][j] = DisciplinaEHorarios[j]         
        
horariosOcupados = []

for i in range(quantidadeDeMaterias):
    for j in range(1,7):
        if TabelaDeHorarios[i][j] == '':
            break
        
        Materia        = TabelaDeHorarios[i][0]
        DiaHorarioAula = TabelaDeHorarios[i][j]
        
        horario     = int(DiaHorarioAula[1:3])
        diaDaSemana = int(DiaHorarioAula[0])
        aulas       = int(DiaHorarioAula[-1])
        
        horariosOcupados.append((diaDaSemana, Materia, horario, aulas))
        
            
horariosOcupados.sort()
choque = False

for horariosDaMateriaTestada in horariosOcupados:
    
    if choque:
        break
    
    diaDaSemana = horariosDaMateriaTestada[0]
    materiaTestada     = horariosDaMateriaTestada[1]
    horario     = horariosDaMateriaTestada[2]
    aulas       = horariosDaMateriaTestada[3]
    
    
    for horariosDaMateriaComparada in horariosOcupados:
        
        if choque:
            break
        
        materiaComparada = horariosDaMateriaComparada[1]
        
        
        if materiaTestada != materiaComparada and diaDaSemana == horariosDaMateriaComparada[0]:
            for i in range(aulas):
                if horario + i == horariosDaMateriaComparada[2]:
                    choque = True 
                    break
                
                   
print(materiaTestada, materiaComparada)
            
            
        