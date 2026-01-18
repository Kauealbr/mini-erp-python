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



if __name__ == "__main__":
    c = Cliente(1, "João", "joao@email.com", "11999999999")
    print(c.nome, c.email, c.telefone)
