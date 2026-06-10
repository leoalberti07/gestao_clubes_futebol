from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jogadores = []
posicoes = ["GOL", "ZAG", "LAT", "MC", "MEI", "PE", "PD", "ATA"]
situacoes = ["ATIVO", "EMPRESTADO", "LESIONADO", "INATIVO"]

@app.route("/jogadores")
def pagina_jogadores():
    return render_template("jogadores.html")

@app.route("/cadastrar_jogador_web", methods=["POST"])
def cadastrar_jogador_web():
    nome = request.form.get("nome_atleta")
    posicao = request.form.get("posicao_atleta").upper()
    situacao = request.form.get("situacao_atleta").upper()
    historico = request.form.get("historico_atleta")

    if posicao not in posicoes:
        return f"Erro: Posicao invalida! Escolha entre: {posicoes}", 400

    if situacao not in situacoes:
        return f"Erro: Situacao invalida! Escolha entre: {situacoes}", 400

    jogador = {
        "nome": nome,
        "posicao": posicao,
        "situacao": situacao,
        "historico": historico
    }
    
    jogadores.append(jogador)
    return redirect(url_for('pagina_jogadores'))

@app.route("/atualizar_jogador_web", methods=["POST"])
def atualizar_jogador_web():
    nome_pesquisa = request.form.get("nome_atualizar")
    nova_situacao = request.form.get("nova_situacao").upper()
    novo_historico = request.form.get("novo_historico")

    if nova_situacao not in situacoes:
        return f"Erro: Situacao invalida! Escolha entre: {situacoes}", 400

    achou = False
    for jogador in jogadores:
        if jogador["nome"].lower() == nome_pesquisa.lower():
            jogador["situacao"] = nova_situacao
            jogador["historico"] += f" | {novo_historico}"
            achou = True
            break

    if not achou:
        return f"Erro: Jogador '{nome_pesquisa}' nao encontrado!", 404

    return redirect(url_for('pagina_jogadores'))

if __name__ == "__main__": 
    app.run(debug=True)