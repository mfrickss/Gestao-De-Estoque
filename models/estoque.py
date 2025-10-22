from .produto import Produto
from rich.console import Console
from rich.table import Table
from factories.produto_factory import ProdutoFactory

class Estoque: 
    def __init__(self, produtosIniciais=None):
        self.produtos = produtosIniciais if produtosIniciais is not None else []

    def getProdutos(self):
        console = Console()

        table = Table(title="Lista de produtos", show_header=True, header_style="bold magenta")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Nome", style="green")
        table.add_column("Quantidade", justify="right", style="yellow")
        table.add_column("Preço", style="blue" )

        for produto in self.produtos:
            table.add_row(
                str(produto.id),
                produto.nome,
                str(produto.quantidade),
                f"R${produto.preco:.2f}"
            )
        
        console.print(table)

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