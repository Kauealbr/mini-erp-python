class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
            return f"ID: {self.id} | {self.nome} | R$ {self.preco:.2f} | Estoque: {self.quantidade}" 
    
class Cliente:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone


class ItemVenda:
    def __init__(self, id, produto_id, quantidade, preco_unitario):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario 


class Venda:
    def __init__(self, id, cliente_id, data, total, itens=None):
        self.id = id
        self.cliente_id = cliente_id
        self.data = data
        self.total = total
        self.itens = itens or []


