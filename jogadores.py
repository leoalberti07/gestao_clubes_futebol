jogadores = []
posicoes = ["GOL", "ZAG", "LAT", "MC", "MEI", "PE", "PD","ATA"]
situacoes = ["ATIVO","EMPRESTADO","LESIONADO","INATIVO",]


def cadastrar_jogador():
   nome = input("digite o nome do atetla: ")
   while True:
       posicao = input(f"Posição {posicoes}: ").upper()
    
       if posicao in posicoes:
          break
       print("posição invalida.") 

   while True:
        situacao = input(f"Situação {situacoes}: ").upper()
    
        if situacao in situacoes:
          break
        print("situação invalida.")
   historico = input("historico do jogador: ") 
   
   jogador = {
        "nome": nome,
        "posicao": posicao,
        "situacao": situacao,
        "historico": historico
    }
   jogadores.append(jogador)
   print("Jogador cadastrado com sucesso!")
def listar_jogadores():
    if not jogadores:
        print("Nenhum jogador cadastrado.")
        return
    print("\n=== JOGADORES ===")
    for i, jogador in enumerate(jogadores):
        print(f"\nID: {i}")
        print(f"Nome: {jogador['nome']}")
        print(f"Posição: {jogador['posicao']}")
        print(f"Situação: {jogador['situacao']}")
        print(f"Histórico: {jogador['historico']}")


def atualizar_jogador():
    if not jogadores:
        print("Nenhum jogador cadastrado.")
        return
    try:
        id_jogador = int(input("ID do jogador:"))
    except ValueError:
        print("digite um numero valido.")
        return
    
    if id_jogador < 0 or id_jogador >= len(jogadores):
        print("ID inválido.")
        return
    
    nova_situacao = input("Nova situação: ").upper()

    if nova_situacao not in situacoes:
        print("Situação inválida.")
        return
    
    jogadores[id_jogador]["situacao"] = nova_situacao

    novo_historico = input("atualização do histórico: ")
    jogadores[id_jogador]["historico"] += f" | {novo_historico}"
    print("Jogador atualizado com sucesso!")


def gerenciar_jogadores():
    while True:
        print("\n=== GERENCIAR JOGADORES ===")
        print("1. Cadastrar jogador")
        print("2. Listar jogadores")
        print("3. Atualizar jogador")
        print("4. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_jogador()
        elif escolha == "2":
            listar_jogadores()
        elif escolha == "3":
            atualizar_jogador()
        elif escolha == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":   
    gerenciar_jogadores()

