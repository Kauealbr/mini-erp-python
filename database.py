import sqlite3
from models import Produto


def conectar():
    return sqlite3.connect("mini_erp.db")


def criar_tabela_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

def inserir_produto(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
        (nome, preco, quantidade)
    )

    conexao.commit()
    conexao.close()


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
    linhas = cursor.fetchall()

    produtos = []
    for linha in linhas:
        produto = Produto(
            id=linha[0],
            nome=linha[1],
            preco=linha[2],
            quantidade=linha[3]
        )
        produtos.append(produto)

    conexao.close()
    return produtos


def atualizar_produto(produto_id, novo_preco, nova_quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE produtos
        SET preco = ?, quantidade = ?
        WHERE id = ?
        """,
        (novo_preco, nova_quantidade, produto_id)
    )

    conexao.commit()
    conexao.close()

def deletar_produto(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM produtos WHERE id = ?",
        (produto_id,)
    )

    conexao.commit()
    conexao.close()



         