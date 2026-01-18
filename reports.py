from database import conectar
import sqlite3
from database import DB_PATH

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

def relatorio_vendas_por_periodo(data_inicio, data_fim):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT SUM(total)
        FROM vendas
        WHERE data BETWEEN ? AND ?
    """, (data_inicio, data_fim))

    total = cursor.fetchone()[0]
    conexao.close()

    return total or 0

def relatorio_produtos_mais_vendidos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.nome,
            SUM(iv.quantidade) AS total_vendido
        FROM itens_venda iv
        JOIN produtos p ON iv.produto_id = p.id
        GROUP BY p.nome
        ORDER BY total_vendido DESC
    """)

    resultados = cursor.fetchall()

    conn.close()

    return resultados


    conn.close() 


def relatorio_faturamento_por_produto():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.nome,
            SUM(iv.quantidade * iv.preco_unitario) AS faturamento
        FROM itens_venda iv
        JOIN produtos p ON iv.produto_id = p.id
        GROUP BY p.nome
        ORDER BY faturamento DESC
    """)

    resultados = cursor.fetchall()
    conn.close()

    return resultados 

def relatorio_cliente_mais_ativo():
    import sqlite3
    from database import DB_PATH

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.nome, SUM(v.total) AS total_gasto
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
        GROUP BY c.nome
        ORDER BY total_gasto DESC
    """)

    resultados = cursor.fetchall()
    conn.close()
    return resultados






