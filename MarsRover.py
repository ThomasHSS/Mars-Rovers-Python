'''
Created on 28 de mai de 2017

@author: Thomas Henrique - https://github.com/ThomasHSS/Mars-Rovers-Python

O codigo abaixo apresenta uma resolucao para o desafio back-end Jr (Mars Rover). 

'''
from test.test_cmath import INF



pontosCardeais = "NESW"   
'''Variavel com as siglas das posicoes cardeais (North - N, East - E, South - S, West - W)'''

movimentos = [(0,1), (1,0), (0, -1), (-1, 0)]   
''''Vetor com as posicoes para a movimentar o rover'''

plator = (5,5) #tamnho do plator

varMovimento = "LRM"
'''Vetor com os dados para a movimentacao do rover'''

def girarR(pCardeal): 
    '''Calcula a direcao cardeal do rover a direita'''   
    position =  pontosCardeais.index(pCardeal) + 1   
    posCard = pontosCardeais[position % 4] 
    return posCard 

             
def girarL(pCardeal): 
    '''Calcula a direcao cardeal do rover a esquerda'''
    position =  pontosCardeais.index(pCardeal) - 1 
    posCard = pontosCardeais[position % 4] 
    return posCard   


def mover(corXY, posC): 
    '''Calcula a movimentacao do rover nas coordenadas xy'''   
    corXY = (corXY[0] + movimentos[posC][0], corXY[1] + movimentos[posC][1])
    return corXY


def verificaCoordenadas(coordenadas):
    '''Valida os dados de entrada da coordenada inicial do rover '''
    for c in range(len(coordenadas)):
        if type(coordenadas[c]) is int:   
            if (coordenadas[c] < 0) | ( coordenadas[c] > plator[1]): 
                return False 
    return True
           

def verificaPCardeal(pCardeal):
    '''Valida a posicao cardeal de entrada do rover'''
    if pCardeal in pontosCardeais:
        return True
    else:
        return False


def verificaMovimentos(cmds):
    '''Valida os dados de entrada para o comando do rover'''  
    for c in cmds:
        if c not in varMovimento:
            return False
    return True    


def exeComandos(coordenadas, pCardeal, cmds):  
    '''Executa os comandos do rover'''  
    
    if verificaCoordenadas(coordenadas) & verificaMovimentos(cmds) & verificaPCardeal(pCardeal) :
        for c in cmds:    
            if (c == 'R'):
                pCardeal = girarR(pCardeal) 
                 
                 
            elif (c == 'L'):
                pCardeal = girarL(pCardeal)
                
                
            elif (c == 'M'):
                coordenadas = mover(coordenadas, pontosCardeais.index(pCardeal))
        print(coordenadas, pCardeal)
    else:
        print("Entrada de dados invalida")
                
    
    
"""TESTES"""

plator(5,5)
exeComandos((1,2), 'N',"LMLMLMLMM")
exeComandos((3, 3), 'E', "MMRMMRMRRM")

            