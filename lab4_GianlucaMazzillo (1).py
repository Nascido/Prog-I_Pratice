#Gianluca Mazzillo
#DRE: 121085969


#Questão 1:

def desconto (v1,v2,v3):
    '''calcula o valor do desconto(d) que será aplicado no valor total(v)'''
    v=v1+v2+v3
    d=min (v1/100,v2/100,v3/100)
    return valorDoDesconto (v,d)

def valorComDesconto(v1,v2,v3):
    '''calcula o valor final com a aplicação do desconto'''
    return (v1+v2+v3)-desconto(v1,v2,v3)

#testes:
#valorComDesconto (10,40,60)
#99.0
#valorComDesconto(20,40,80)
#112.0
#valorComDesconto (30,50,90)
#119.0

#Questão 2:

def feliz (I):
    '''funçao que acrescenta caracteres da nona casa a partir de um indice I
int ->str'''
    str = 'Feliz natal!!'
    return str[0:9]+str[9]*I+str[9:]

#testes:
#>>> feliz(5)
#'Feliz nataaaaaal!!'
#>>> feliz(8)
#'Feliz nataaaaaaaaal!!'
#>>> feliz(50)
#'Feliz nataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaal!!'

#Questão 3:

def idade (anos,meses,dias):
    '''função que retorna o valor correto da idade de uma pessoa
int,int,int->str'''
    anos = ((dias//365) + anos) + (meses//12) 
    meses= dias%365//30  
    dias= dias%365%30 
    return str(anos)+' ano(s) '+str(meses)+' mês(es) '+str(dias)+' dia(s) '

#testes:
#>>> idade (0,0,395)
#'1 ano(s) 1 mês(es) 0 dia(s) '
#>>> idade (1,13,398)
#'3 ano(s) 1 mês(es) 3 dia(s) '
#>>> idade (1,12,365)
#'3 ano(s) 0 mês(es) 0 dia(s) '

#Questão 4:
def filtra_pares(a,b,c,d):
    '''função que retorna os numeros pares de um parametro
int->tuple'''
    pares = ()
    if ((a,b,c,d)[0]%2) == 0:
        pares = pares + ((a,b,c,d)[0],)
    if ((a,b,c,d)[1]%2) == 0:
        pares = pares + ((a,b,c,d)[1],)
    if ((a,b,c,d)[2]%2) == 0:
        pares = pares + ((a,b,c,d)[2],)
    if ((a,b,c,d)[3]%2) == 0:
        pares = pares + ((a,b,c,d)[3],)
    return pares

#testes
#>>> filtra_pares (98,12,4,22)
#(98, 12, 4, 22)
#>>> filtra_pares (12,23,98,5)
#(12, 98)
#>>> filtra_pares (13,25,5,23)
#()

#Questão 5:

def pomekon (Ai1,Di1,Li1,Ai2,Di2,Li2):
    '''função que calcula o resultado de um duelo de pomekon 
int,int,int,int,int,int->str'''
    bonus1 = Li1//3
    bonus2 = Li2//3
    valorGolpeDabriel = (Ai1+Di1)/2 + bonus1
    valorGolpeGuarte = (Ai2+Di2)/2 + bonus2
    (1<=Ai1,Di1<=100, 1<=Li1<=50)
    (1<=Ai2,Di2<=100, 1<=Li2<=50)
    if valorGolpeDabriel>valorGolpeGuarte:
        return 'Dabriel'
    elif valorGolpeDabriel == valorGolpeGuarte:
        return 'Empate'
    else:
        return 'Guarte'

#testes:
#>>> pomekon (5,5,5,3,3,3)
#'Dabriel'
#>>> pomekon (2,2,2,6,6,6)
#'Guarte'
#>>> pomekon (8,8,8,8,8,8)
#'Empate'

#Questão 6:

def taxaDeImposto (renda):
    '''retorna o valor do imposto a ser pago a partir da renda do cidadão
float->str'''
    if renda<2000:
        return 'Insento'
    elif 2000.01<=renda<3000:
        return 'R$ ' + str(renda*0.08) 
    elif 3000.01<renda<4500:
        return 'R$ ' +str(renda*0.18) 
    else:
        return 'R$ ' + str(renda*0.28)

#testes:
#>>> taxaDeImposto (1000)
#'Insento'
#>>> taxaDeImposto (3100)
#'R$ 558.0'
#>>> taxaDeImposto (6000)
#'R$ 1680.0000000000002'

#Questão 7:

def dna(sequencia):
    '''retorna em string se a bacteria é ou não resistente a partir
dos compostos de proteina A,T,G,C
str->str'''
    if 'CGT' in sequencia:
        return "Resistente"
    else:
        return "Nao resistente"

#testes:
#>>> dna ('ATCGT')
#'Resistente'
#>>> dna ('CGCGTA')
#'Resistente'
#>>> dna ('ATCTGA')
#'Nao resistente'


    
    


    
