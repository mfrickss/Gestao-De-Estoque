from models.produto import Produto

class ProdutoFactory:
    @staticmethod
    def calcularId(getProdutos):
        if not getProdutos:
            return 1
        return max(p.id for p in getProdutos) + 1
    
    @staticmethod
    def criarNovoProduto(nome, qtd, preco, getProdutosAtual):
        novoId = ProdutoFactory.calcularId(getProdutosAtual)

        novoProduto = Produto(nome, qtd, preco)
        novoProduto.id = novoId

        return novoProduto
    