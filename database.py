import sqlite3


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
    produtos = cursor.fetchall()

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

if __name__ == "__main__":
    produtos = listar_produtos()
    print("ANTES:", produtos)

    atualizar_produto(1, 30.00, 5)

    produtos = listar_produtos()
    print("DEPOIS:", produtos)

            
         