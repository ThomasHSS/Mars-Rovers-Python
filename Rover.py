'''
Created on 28 de mai de 2017

@author: Thomas Henrique - https://github.com/ThomasHSS/Mars-Rovers-Python

O codigo abaixo apresenta uma resolucao para o desafio back-end Jr (Mars Rover). 

'''



pCardeais = "NESW"   
'''Variavel com as siglas das posicoes cardeais (North - N, East - E, South - S, West - W)'''

movimentos = [(0,1), (1,0), (0, -1), (-1, 0)]   
"""Vetor com as posicoes para a movimentar o rover """


def girarR(pCardeal): 
    '''Calcula a direcao cardeal do rover a direita'''   
    position =  pCardeais.index(pCardeal) + 1   
    posCard = pCardeais[position % 4] 
    return posCard 
    
          
def girarL(pCardeal): 
    '''Calcula a direcao cardeal do rover a esquerda'''
    position =  pCardeais.index(pCardeal) - 1 
    posCard = pCardeais[position % 4] 
    return posCard   


def mover(corXY, posC): 
    '''Calcula a movimentacao do rover nas coordenadas xy'''   
    corXY = (corXY[0] + movimentos[posC][0], corXY[1] + movimentos[posC][1])
    return corXY
    

def exeComandos(coordenadas, pCardeal, cmds):  
    '''Executa os comandos do rover'''  
    
    for c in cmds:    
        if (c == 'R'):
            pCardeal = girarR(pCardeal) 
             
             
        elif (c == 'L'):
            pCardeal = girarL(pCardeal)
            
            
        elif (c == 'M'):
            coordenadas = mover(coordenadas, pCardeais.index(pCardeal))
            
    print(coordenadas, pCardeal)
    
"""TESTES"""

exeComandos((1,2), 'N',"LMLMLMLMM")
exeComandos((3, 3), 'E', "MMRMMRMRRM")
exeComandos((3, 5), 'S', "MLRMMRMMLLR")
exeComandos((1,1), 'E', "MLMRMRRMMLLR")
exeComandos((0, 0), 'W', "LMMRMRRMMMLR")
        