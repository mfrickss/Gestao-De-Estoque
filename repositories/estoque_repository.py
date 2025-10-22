import pandas as pd
import json
from models.produto import Produto

class EstoqueRepository: 

    def salvarEmJson(self, nomeArquivo, listaProdutos):
        try:
            if not nomeArquivo.endswith(".json"):
                nomeArquivo += ".json"

            produtos_dict = []

            for produto in listaProdutos:
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
                produtosCarregados = []
                
                for item in dados:
                    produto = Produto(item['nome'], item['quantidade'], item['preco'])
                    produto.id = item['id']
                    produtosCarregados.append(produto)

            print(f"Dados carregados com sucesso de {nomeArquivo}!")
            return produtosCarregados

        except FileNotFoundError:
            print(f"Arquivo {nomeArquivo} não encontrado! O estoque será iniciado vazio.")
        except Exception as e:
            print(f"ERROR ao carregar JSON: {str(e)}")
            return []
            
    def exportarCsv(self, nomeArquivo, listaProdutos):
        if not listaProdutos:
            print("Não há produtos para exportar!")
            return
            
        dadosProduto = [
            {"id": produto.id, "nome": produto.nome, "quantidade": produto.quantidade, "preço": produto.preco}
            for produto in listaProdutos
            ]

        df = pd.DataFrame(dadosProduto)

        try:
            df.to_csv(nomeArquivo, index= False, encoding="utf-8")
            print(f"Dados exportados com sucesso para o arquivo {nomeArquivo}")
        except Exception as e:
            print(f"ERRO: {e}")