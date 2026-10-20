class Produto:
    def __init__(self, nome,preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade > self.estoque:
            return False
        self.estoque -= quantidade
        return True
    
    def mostrar(self):
        print(self.nome, self.estoque)
        
mouse = Produto("Mouse", 45.9, 12)
cabo = Produto("Cabo", 25.0, 2)

mouse = Produto("Mouse", 45.9, 12)
print(mouse.vender(5))  # True
mouse.mostrar()  # Mouse 7
print(mouse.vender(50))  # False