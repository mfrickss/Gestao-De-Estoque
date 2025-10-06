# def adicionarProduto(nome, qtd):
#     if any(produto['nome'] == nome for produto in estoque):
#         print("Produto já cadastrado!")
#         return 
#     if estoque:
#         novo_id = max(produto['id'] for produto in estoque) + 1
#     else:
#         novo_id = 1

#     novoProduto = {'id': novo_id, 'nome': nome, 'qtd': qtd}
#     estoque.append(novoProduto)

#     print(f"Produto '{nome}' adicionado com sucesso!")
#     return novoProduto

from models import Produto, Estoque 

estoque_manager = Estoque()

estoque_manager.carregarJson("estoque")

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
                estoque_manager.listar_produtos()
            case 2:
                nome = input("Informe o nome do produto: ").capitalize()
                qtd = int(input("Informe a quantidade do produto: "))
                preco = float(input("Informe o preço do produto: "))
                estoque_manager.adicionarProduto(nome, qtd, preco)
            case 3:
                id_produto = int(input("Informe o id do produto: "))
                nova_qtd = int(input("Informe a nova quantidade do produto: "))
                estoque_manager.atualizarQuantidade(id_produto, nova_qtd)
            case 4:
                id_produto = int(input("Informe o ID do produto: "))
                novo_preco = float(input("Informe o preço do produto: "))
                estoque_manager.atualizarPreco(novo_preco)
            case 5:
                id_produto = int(input("Informe o id do produto que desejas remover: "))
                estoque_manager.removerProduto(id_produto)
            case 6:
                estoque_manager.exportarCsv("meuEstoque.csv")
            case 0: 
                estoque_manager.salvarEmJson("estoque")
                print("Obrigado por utilizar nosso sistema. Até logo!")
            case _:
                print("Opção inválida!")
    except ValueError:
        print("ERRO! Por favor, digite um número válido!")



