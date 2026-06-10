import sqlite3
import io

brasileiro = [
    48100000, 45700000, 43300000, 40900000, 38500000,
    36100000, 33700000, 31300000, 28800000, 26400000,
    20700000, 19200000, 17800000, 17300000, 16800000,
    16300000, 0, 0, 0, 0
]

def importar_banco(competicoes, database):
    try:
        conn = sqlite3.connect(competicoes)
        cursor = conn.cursor()
        with io.open(database, 'r', encoding='utf-8') as f:
            sql_content = f.read()
            conn.commit
            print(f"Banco {competicoes} importado com sucesso")
    except sqlite3.Error as e:
        print("Erro ao importar")
    finally:
        if 'conn' in locals():
            conn.close()


def calculo_brasileirão(colocao ):
    return brasileiro[colocao]
    