class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

if __name__ == "__main__":
    p = Produto(1, "Arroz", 25.90, 10)
    print(p.nome, p.preco, p.quantidade)
