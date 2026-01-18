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


if __name__ == "__main__":
        criar_tabela_produtos()
        print("Tabela de produtos criada com sucesso!")
            
         