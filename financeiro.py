banco_temporario = []

def calcular_saldo():
    if len(banco_temporario) == 0:
        print("Nenhuma movimentação registrada até o momento.")
        return 0, 0, 0
    total_receita = 0
    total_despesa = 0
    for i in banco_temporario:
        if i["tipo"] == "receita":
            total_receita += i["valor"]
        else:
            total_despesa += i["valor"]
    total = total_receita - total_despesa
    return total, total_receita, total_despesa

def cadastro_transacoes(tipo, valor, descricao):
    transacao = {"tipo": tipo,"valor": valor, "descricao": descricao}
    banco_temporario.append(transacao)
    print("transação adicionada com sucesso!")


def menu():
    while True:
        print("="*30)
        print("="*30)
        print("BEM VINDO AO SETOR FINANCEIRO")
        print("="*30)
        print("="*30)
        print("\n1 - CADASTRAR TRANSAÇÃO\n2 - EXIBIR RELATÓRIOS\n3 - SAIR")
        resposta = validar_resp(3)
        if resposta == 1:
            print("\n1 - RECEITA\n2 - DESPESA")
            resposta = validar_resp(2)
            if resposta == 1:
                tipo = "receita"
            else:
                tipo = "despesa"
            transacoes(tipo)
        elif resposta == 2:
            gerar_relatorio()
        elif resposta == 3:
            break

def gerar_relatorio():
    saldo_total, receita_total, despesa_total = calcular_saldo()
    print("======== RELATÓRIO ========")
    print("histórico de transações:")
    for item in banco_temporario:
        print(f"- {item['descricao']}: R${item['valor']:.2f} ({item['tipo'].upper()})")
    print("===========================")
    print(f"receita total: R${receita_total:.2f}")  
    print(f"despesa total: R${despesa_total:.2f}")
    print(f"saldo total:   R${saldo_total:.2f}")
    if saldo_total < 0:
        print("ATENÇÃO o clube está no vermelho!!")
    else:
        print("o clube está no AZUL!!")

def validar_resp(resp_possiveis):
    while True:
        try:
            resp = int(input("\nescolha uma opção: "))
            if resp in range(1, (resp_possiveis + 1)):
                return resp
            else:
                print(f"escolha uma opção valida! (1 ate {resp_possiveis})")
        except ValueError:
            print("valor invalido!")

def transacoes(tipo):
    valor = get_valor_float()
    descricao = get_descricao(tipo)
    cadastro_transacoes(tipo, valor, descricao)

def get_int_desc(possiveis):
    while True:
        try:
            val = int(input("informe o numero da opção que te satisfaz: "))
            if val in range(1, len(possiveis) + 1):
                return val
            else: 
                print("valores invalidos!")
        except ValueError:
            print("valores invalidos!")

def get_valor_float():
    while True:
        try:
            val = float(input("informe o valor da transação: R$"))
            if val > 0:
                return val
            else: 
                print("valores invalidos!")
        except ValueError:
            print("valores invalidos!")

def get_descricao(tipo):
    if tipo == "receita":
        possiveis_receitas = [
            "Patrocínio Máster",
            "Patrocínios Secundários",
            "Sócio-Torcedor",
            "Bilheteria (Ingressos)",
            "Venda de Produtos Licenciados",
            "Cotas de TV e Direitos de Transmissão",
            "Premiações de Campeonatos",
            "Venda / Transferência de Atletas",
            "Aluguel do Estádio / Eventos"
            ]
        for i in range(len(possiveis_receitas)):
            print(f"{i + 1} - {possiveis_receitas[i]}")
        return possiveis_receitas[get_int_desc(range(len(possiveis_receitas))) - 1]
    
    else:
        possiveis_despesas = [
            "Salário do Elenco (Jogadores)",
            "Salário da Comissão Técnica e Staff",
            "Manutenção do Estádio e Gramado",
            "Despesas com Viagens e Hospedagem",
            "Contratação / Compra de Novos Atletas",
            "Impostos e Taxas da Federação",
            "Logística e Equipamentos (Material Esportivo)",
            "Contas Gerais (Água, Luz, Internet do CT)",
            "Investimento nas Categorias de Base"
            ]
        
        for i in range(len(possiveis_despesas)):
            print(f"{i + 1} - {possiveis_despesas[i]}")
        return possiveis_despesas[get_int_desc(range(len(possiveis_despesas))) - 1]

menu()
        