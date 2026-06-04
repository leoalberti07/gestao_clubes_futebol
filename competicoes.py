list_comp = ["Brasileirão", "Libertadores", "Copa do Brasil"]
premio_libertadores = [
    6440000,    # oitavas
    9000000,    # quartas
    11850000,   # semi
    36000000,   # vice
    129000000   # campeão
]
premio_brasileiro = [
    48100000, 45700000, 43300000, 40900000, 38500000,
    36100000, 33700000, 31300000, 28800000, 26400000,
    20700000, 19200000, 17800000, 17300000, 16800000,
    16300000, 0, 0, 0, 0
]
premio_copa_do_brasil =[ 2000000,   # 5ª fase
    3000000,   # oitavas
    4000000,   # quartas
    9000000,   # semi
    34000000,  # vice
    78000000   # campeão
]
def main(lista_resultados,lista_colocacoes,dados_competicao,premio_liberta_total,premio_copa_total ):
    lista_colocacoes = colocacao(list_comp)
    lista_resultados = resultados(list_comp)
    dados_competicao = competicao(lista_colocacoes,list_comp,lista_resultados)
    premio_liberta_total = prize_liberta(
    lista_resultados,
    lista_colocacoes)
    premio_copa_total = prize_copa_do_brasil(
    dados_competicao,
    lista_colocacoes)
    while True:
        valor = validar_resp(4, f"Digite 1 - Resultados\nDigite 2 - Competição\nDigete 3 - Premiações\n Digite 4 - Sair ")
        if valor == 1:
            return print(lista_resultados)
        elif valor == 2:
            return print(competicao)
        elif valor == 3:
            msg = (("Digite 1 - Brasileirão\n" 
            "Digite 2 - Libertadores,\nDigite 3 - Copa do Brasil: "))
            opcao_de_campeonato = validar_resp(3, msg)
            if opcao_de_campeonato == 1:
                return print(premio_brasileiro[lista_colocacoes[0]])
            elif opcao_de_campeonato == 2:
                return  print(premio_liberta_total)
            elif opcao_de_campeonato == 3:
                return print(premio_copa_total)
        else:
            break

def validar_resp(resp, msg):
    while True:
        try:
            validar = int(input(msg))
            if validar in range(1, (resp + 1)):
                return validar
            else:
                print("Valor invalido escolha um valor dentro do range")
        except ValueError:
            print("Fora do padrão")

def resultados(list_comp:list):
    list_resultados = []
    for comp in list_comp:
        msg = (f"Digite o número de vitorias {comp}: ")
        if comp == "Brasileirão":
            resp = 38
        elif comp == "Libertadores":
            resp = 6
        elif comp == "Copa do Brasil":
            resp = 9
        list_resultados.append(validar_resp(resp,msg))
    return list_resultados

def competicao(colocacoes: list, list_comp: list,list_resultados: list):
    return {"competicoes": list_comp, "colocacoes": colocacoes, "Resultados": list_resultados, "Premios": [premio_brasileiro,premio_libertadores,premio_copa_do_brasil]}

def colocacao(colocacoes:list):
    colocacoes = []
    for comp in list_comp:
        msg = (f"Digite a colocação do time na competição {comp}: ")
        if comp == "Brasileirão":
            resp = 20 
        elif comp == "Libertadores":
            msg = (f"Digite a fase que o time parou na {comp}:\nDigite 1- Fase de Grupos\nDigite 2- Oitavas\nDigite 3-Quartas\nDigite 4 - Semifinais\nDigite 5- vice\nDigite 6- Campeão \n")
            resp = 6
        elif comp == "Copa do Brasil":
            msg = (f"Digite a fase que o time parou na {comp}:\nDigite 1- 5ª Fase\nDigite 2- Oitavas\nDigite 3-Quartas\nDigite 4 - Semifinais\nDigite 5- vice\nDigite 6- Campeão\n ")
            resp = 6
        colocacoes.append(validar_resp(resp,msg))
    return colocacoes


def prize_liberta(resultados:list , colocacoes:list):
    fase_de_grupos = 5150000 + resultados[1] * 1750000
    premios = [fase_de_grupos] + premio_libertadores
    if colocacoes[1] == 6:
        return premios[:colocacoes[1]] - premios[4]
    return sum(premios[:colocacoes[1]])
def prize_copa_do_brasil(competicao, colocacoes):
    if premio_brasileiro(colocacao[2]) == premio_brasileiro[6]:
          sum(premio_copa_do_brasil[:colocacoes[2]]) - premio_brasileiro[5] 
    return sum(premio_copa_do_brasil[:colocacoes[2]]) 

    
main(resultados, competicao, colocacao,prize_liberta,prize_copa_do_brasil)