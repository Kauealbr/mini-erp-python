import sqlite3
from models import Produto
from models import Cliente


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


         