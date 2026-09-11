# # GerirFut

Sistema web de gestão para clubes de futebol, construído em Flask. Centraliza o controle do elenco, o fluxo financeiro do clube, o histórico de competições disputadas e o registro de contratações de novos atletas.

## Funcionalidades

### Jogadores
- Cadastro de atletas com nome, posição, situação (ativo, emprestado, lesionado, inativo), histórico e salário.
- Listagem do elenco em um histórico pesquisável.
- Edição dos dados de um jogador já cadastrado.

### Financeiro
- Dashboard com total de receitas, total de despesas e saldo atual, com gráfico de rosca (Chart.js) mostrando a divisão entre entradas e saídas.
- Filtro do painel por período (data início/fim).
- Registro de novas transações (receita ou despesa), com categorias pré-definidas como patrocínio, bilheteria, salários, manutenção de estádio, entre outras.
- Listagem e busca de transações por descrição, com opção de exclusão.
- Geração automática de uma transação de despesa correspondente à folha salarial total do elenco.

### Competições
- Cadastro de campeonatos disputados, com colocação final, premiação, número de jogos, vitórias, empates e derrotas.
- O valor da premiação gera automaticamente uma transação de receita no financeiro.
- Listagem e busca de competições cadastradas.

### Contratações
- Cadastro de contratações de atletas, com nome, posição, clube de origem, valor da transferência e salário.
- Cada contratação gera automaticamente uma transação de despesa no financeiro e um novo registro na lista de jogadores.
- Histórico de contratações com busca por nome.

## Estrutura do projeto

```
.
├── app/
│   ├── __init__.py     # criação da aplicação Flask, configuração do banco e migrações
│   ├── routes.py        # rotas e lógica de cada página
│   ├── models.py        # modelos do banco de dados (SQLAlchemy)
│   ├── form.py           # formulários (Flask-WTF) e regras de validação
│   ├── templates/        # páginas HTML (Jinja2)
│   └── static/
│       └── css/
│           └── style.css # estilos da interface, incluindo o menu lateral retrátil
├── migrations/            # histórico de versões do schema do banco (Flask-Migrate)
├── database.db            # banco de dados SQLite
├── main.py                 # ponto de entrada da aplicação
└── README.md
```

## Tecnologias utilizadas

- **Flask** — framework web
- **Flask-SQLAlchemy** — ORM para o banco de dados
- **Flask-Migrate** — controle de versões do schema do banco (baseado em Alembic)
- **Flask-WTF / WTForms** — criação e validação de formulários
- **SQLite** — banco de dados
- **Bootstrap 5** — estilização da interface
- **Chart.js** — gráfico do painel financeiro

## Modelos de dados

- **Jogador**: nome, posição, situação, histórico e salário do atleta.
- **Transacao**: tipo (receita/despesa), valor, descrição e data de cada movimentação financeira.
- **Competicoes**: nome do campeonato, colocação, premiação, jogos, vitórias, empates e derrotas.
- **Transferencias**: nome do atleta, posição, clube anterior, valor da transferência e salário.
- **Historico**: descrição e data de eventos associados a um jogador específico.

## Como executar

1. Instale as dependências:
   ```bash
   pip install flask flask-sqlalchemy flask-migrate flask-wtf
   ```
2. Rode a aplicação:
   ```bash
   python main.py
   ```
3. Acesse `http://localhost:5000` no navegador.

O banco de dados SQLite (`database.db`) já é criado automaticamente pela configuração em `app/__init__.py`. Caso o schema precise ser atualizado depois de alterações em `models.py`, use os comandos do Flask-Migrate (`flask db migrate` e `flask db upgrade`).

## Rotas principais

| Rota                          | Descrição                                   |
|--------------------------------|-----------------------------------------------|
| `/`                             | Página inicial com resumo geral do clube      |
| `/jogadores`                    | Cadastro e listagem de jogadores              |
| `/historico`                    | Histórico pesquisável de jogadores            |
| `/editar/<id>`                  | Edição de um jogador específico               |
| `/financeiro`                   | Painel financeiro com gráfico e filtros       |
| `/financeiro_transacoes`        | Cadastro de novas transações                  |
| `/financeiro_lista`             | Histórico de transações                       |
| `/gerar_folha`                  | Geração da folha de pagamento do elenco       |
| `/competicoes`                  | Cadastro de competições                       |
| `/competicoes/financeiro`       | Histórico de competições cadastradas          |
| `/contratacoes`                 | Cadastro de contratações                      |
| `/contratacoes/historicos`      | Histórico de contratações                     |
