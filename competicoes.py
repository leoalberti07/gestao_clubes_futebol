from app import *


brasileiro = [
    48100000, 45700000, 43300000, 40900000, 38500000,
    36100000, 33700000, 31300000, 28800000, 26400000,
    20700000, 19200000, 17800000, 17300000, 16800000,
    16300000, 0, 0, 0, 0
]
copa_do_brasil = [
    78000000,  # campeão
    34000000,  # vice-campeão
    9000000,   # semifinal
    4000000,   # quartas de final
    3000000,   # oitavas de final
    2000000    # 5ª fase
]

premio_libertadores = [
    
    6440000,    # oitavas
    9000000,    # quartas
    11850000,   # semi
    36000000,   # vice
    129000000   # campeão
]
def calculo_libertadores(colocacao,vitorias):
    fase_de_grupos = 5150000 + vitorias * 1750000 
    premio_libertadores.append(fase_de_grupos)
    if colocacao == 1:
        return sum(premio_libertadores[:colocacao]) - 36000000
    else: 
        return sum(premio_libertadores[:colocacao])



def calculo_brasileirao(colocacao):

    return brasileiro[colocacao]
    