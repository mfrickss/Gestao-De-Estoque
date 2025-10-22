from models import Produto, Estoque 
from repositories.estoque_repository import EstoqueRepository

estoqueRepo = EstoqueRepository()
estoqueManager = Estoque()
produtosIniciais = estoqueRepo.carregarJson("estoque")
estoqueManager.produtos = produtosIniciais

op = -1
while op != 0:

    print("-" * 10)
    print("GERÊNCIADOR DE ESTOQUE")
    print("-" * 10)
    print("Escolha uma opcão")
    print("1 - Listar produtos")
    print("2 - Adicionar novo produto")
    print("3 - Atualizar quantidade do produto")
    print("4 - Atualizar preço do produto")
    print("5 - Remover produto")
    print("6 - Exportar CSV")
    print("0 - Sair")

    try:
        op = int(input("Escolha uma opcão: "))

        match op:
            case 1:
                estoqueManager.getProdutos()
            case 2:
                nome = input("Informe o nome do produto: ").capitalize()
                qtd = int(input("Informe a quantidade do produto: "))
                preco = float(input("Informe o preço do produto: "))
                estoqueManager.postProduto(nome, qtd, preco)
            case 3:
                idProduto = int(input("Informe o id do produto: "))
                novaQtd = int(input("Informe a nova quantidade do produto: "))
                estoqueManager.putQuantidade(idProduto, novaQtd)
            case 4:
                idProduto = int(input("Informe o ID do produto: "))
                novoPreco = float(input("Informe o preço do produto: "))
                estoqueManager.putPreco(idProduto, novoPreco)
            case 5:
                idProduto = int(input("Informe o id do produto que desejas remover: "))
                estoqueManager.deleteProduto(idProduto)
            case 6:
                estoqueRepo.exportarCsv("meuEstoque.csv", estoqueManager.produtos)
            case 0: 
                estoqueRepo.salvarEmJson("estoque", estoqueManager.produtos)
                print("Obrigado por utilizar nosso sistema. Até logo!")
            case _:
                print("Opção inválida!")

    except ValueError:
        print("ERRO! Por favor, digite um número válido!")



