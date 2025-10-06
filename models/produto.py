class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def atualizarPreco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
        else:
            print(f"ERRO: Informe um valor válido!")