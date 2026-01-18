from database import conectar

def relatorio_estoque():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, quantidade, preco
        FROM produtos
        ORDER BY nome
    """)

    resultados = cursor.fetchall()
    conexao.close()

    return resultados

