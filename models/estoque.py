from .produto import Produto
from views.ProductView import ProdutoView
from factories.produto_factory import ProdutoFactory

class Estoque: 
    def __init__(self, produtosIniciais=None):
        self.produtos = produtosIniciais if produtosIniciais is not None else []

    def getProdutos(self):
        ProdutoView.mostrarProdutos(self.produtos)

    def postProduto(self, nome, qtd, preco):
        for produto in self.produtos:
            if(produto.nome == nome):
                print("Produto já cadastrado!")
                return
    
        novoProduto = ProdutoFactory.criarNovoProduto(nome, qtd, preco, self.produtos)
        self.produtos.append(novoProduto)
        print(f"Produto '{nome}' adicionado com sucesso!")
        return novoProduto

    def putQuantidade(self, id_produto, nova_qtd):
        for produto in self.produtos:
            if(id_produto == produto.id):
                produto.quantidade = nova_qtd
                print(f"A quantidade de {produto.nome} foi atualizada para: {nova_qtd}")
                return
        print("ERRO: Produto não encontrado")

    def putPreco(self, id_produto, novo_preco):
        for produto in self.produtos:
            if(id_produto == produto.id):
                produto.preco = novo_preco
                print(f"O preço de {produto.nome} foi atualizado para: {novo_preco}")
                return
        print("ERRO: Produto não encontrado")   

    def deleteProduto(self, id_produto):
        for produto in self.produtos:
            if(id_produto == produto.id):
                self.produtos.remove(produto)
                print(f"O produto {produto.nome} foi removido com sucesso!")
                return
        raise ValueError("ERRO: Produto não encontrado!")