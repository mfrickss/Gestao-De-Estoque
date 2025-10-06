import json
from .produto import Produto
from rich.console import Console
from rich.table import Table
import pandas as pd

class Estoque: 
    def __init__(self):
        self.produtos = [
            Produto("Caneta", 100, 400),
            Produto("Caderno", 860, 500),
            Produto("Penal", 10, 600),
            Produto("Lapis", 560, 700),
            Produto("Borracha", 1000, 800),
            Produto("Livro", 60, 900)
        ]
        for i, produto in enumerate(self.produtos, 1):
            produto.id = i
    
    def removerProduto(self, id_produto):
        for produto in self.produtos:
            if(id_produto == produto.id):
                self.produtos.remove(produto)
                print(f"O produto {produto.nome} foi removido com sucesso!")
                return
        raise ValueError("ERRO: Produto não encontrado!")
    

    def adicionarProduto(self, nome, qtd, preco):
        for produto in self.produtos:
            if(produto.nome == nome):
                print("Produto já cadastrado!")
                return
            
        novo_id = len(self.produtos) + 1
        novoProduto = Produto(nome, qtd, preco)
        novoProduto.id = novo_id
        self.produtos.append(novoProduto)
        print(f"Produto '{nome}' adicionado com sucesso!")
        return novoProduto


    def atualizarQuantidade(self, id_produto, nova_qtd):
        for produto in self.produtos:
            if(id_produto == produto.id):
                produto.quantidade = nova_qtd
                print(f"A quantidade de {produto.nome} foi atualizada para: {nova_qtd}")
                return
        print("ERRO: Produto não encontrado")

    def atualizarPreco(self, id_produto, novo_preco):
        for produto in self.produtos:
            if(id_produto == produto.id):
                produto.preco = novo_preco
                print(f"O preço de {produto.nome} foi atualizado para: {novo_preco}")
                return
        print("ERRO: Produto não encontrado")   

    def listar_produtos(self):
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


    def salvarEmJson(self, nomeArquivo):
        try:
            if not nomeArquivo.endswith(".json"):
                nomeArquivo += ".json"

            produtos_dict = []

            for produto in self.produtos:
                produtos_dict.append({
                    'id': produto.id,
                    'nome': produto.nome,
                    'quantidade': produto.quantidade,
                    'preco': produto.preco
                })

            with open(nomeArquivo, "w") as arquivo:
                json.dump(produtos_dict, arquivo, indent=4)
            print(f"Estoque salvo com sucesso em {nomeArquivo}!")

        except Exception as e:
            print(f"Erro ao salvar arquivo: {str(e)}")

    def carregarJson(self, nomeArquivo):
        try:
            if not nomeArquivo.endswith(".json"):
                nomeArquivo += ".json"

            with open(nomeArquivo, "r") as arquivo:
                dados = json.load(arquivo)
                self.produtos = []

                for item in dados:
                    produto = Produto(item['nome'], item['quantidade'], item['preco'],)
                    produto.id = item['id']
                    self.produtos.append(produto)

            print(f"Dados carregados com sucesso de {nomeArquivo}!")

        except FileNotFoundError:
            print(f"Arquivo {nomeArquivo} não encontrado!")
        except Exception as e:
            print(f"ERROR: {str(e)}")
        
    
    def exportarCsv(self, nomeArquivo):
        if not self.produtos:
            print("Não há produtos para exportar!")
            return
        
        dadosProduto = [
            {"id": produto.id, "nome": produto.nome, "quantidade": produto.quantidade, "preço": produto.preco}
            for produto in self.produtos
        ]

        df = pd.DataFrame(dadosProduto)

        try:
            df.to_csv(nomeArquivo, index= False, encoding="utf-8")
            print(f"Dados exportados com sucesso para o arquivo {nomeArquivo}")
        except Exception as e:
            print(f"ERRO: {e}")

