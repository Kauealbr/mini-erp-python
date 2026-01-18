import sqlite3
import os
from models import Produto
from models import Cliente
from datetime import date


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "mini_erp.db")

def conectar():
    return sqlite3.connect(DB_PATH)


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

def criar_tabela_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

def inserir_cliente(nome, email, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
    """, (nome, email, telefone))

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

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()

    clientes = []
    for linha in resultados:
        cliente = Cliente(
            id=linha[0],
            nome=linha[1],
            email=linha[2],
            telefone=linha[3]
        )
        clientes.append(cliente)

    conexao.close()
    return clientes

def atualizar_cliente(id, nome, email, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE clientes
        SET nome = ?, email = ?, telefone = ?
        WHERE id = ?
    """, (nome, email, telefone, id))

    conexao.commit()
    conexao.close()

def deletar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?
    """, (id,))

    conexao.commit()
    conexao.close()


def criar_tabela_vendas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            total REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)

    conexao.commit()
    conexao.close()

def criar_tabela_itens_venda():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            FOREIGN KEY (venda_id) REFERENCES vendas(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    """)

    conexao.commit()
    conexao.close()

def buscar_produto_por_id(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos WHERE id = ?", (produto_id,))
    linha = cursor.fetchone()
    conexao.close()

    if linha:
        return linha
    return None
 
def atualizar_estoque(produto_id, nova_quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
    """, (nova_quantidade, produto_id))

    conexao.commit()
    conexao.close()

def criar_venda(cliente_id, itens):
    conexao = conectar()
    cursor = conexao.cursor()

    data_venda = date.today().isoformat()
    total = 0
    produtos_venda = []

    for produto_id, quantidade in itens:
        produto = buscar_produto_por_id(produto_id)

        if not produto:
            conexao.close()
            raise ValueError("Produto não encontrado")

        estoque_atual = produto[3]
        preco = produto[2]

        if quantidade > estoque_atual:
            conexao.close()
            raise ValueError("Estoque insuficiente")

        subtotal = preco * quantidade
        total += subtotal

        produtos_venda.append((produto_id, quantidade, preco))
        # 1. Inserir venda
    cursor.execute("""
        INSERT INTO vendas (cliente_id, data, total)
        VALUES (?, ?, ?)
    """, (cliente_id, data_venda, total))

    venda_id = cursor.lastrowid
    # 2. Inserir itens da venda e atualizar estoque
    for produto_id, quantidade, preco in produtos_venda:
        cursor.execute("""
            INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario)
            VALUES (?, ?, ?, ?)
        """, (venda_id, produto_id, quantidade, preco))

        produto = buscar_produto_por_id(produto_id)
        novo_estoque = produto[3] - quantidade
        atualizar_estoque(produto_id, novo_estoque)
    conexao.commit()
    conexao.close() 






