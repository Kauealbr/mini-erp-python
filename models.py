class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
            return f"ID: {self.id} | {self.nome} | R$ {self.preco:.2f} | Estoque: {self.quantidade}" 


if __name__ == "__main__":
    p = Produto(1, "Arroz", 25.9, 10)
    print(p)
