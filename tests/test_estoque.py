from models import Produto, Estoque 
import pytest

def test_remover_produto_inexistente_lanca_erro():
    estoque = Estoque()
    with pytest.raises(ValueError):
        estoque.removerProduto(999)



def test_adicionar_produto_aumenta_contagem():
    estoque = Estoque()
    contagem_inicial = len(estoque.produtos)


    estoque.adicionarProduto("Teste", 10, 1.99)

    assert len(estoque.produtos) == contagem_inicial + 1
    novo_produto = estoque.produtos[-1]
    assert novo_produto.nome == "Teste"
    assert novo_produto.quantidade == 10
    assert novo_produto.preco == 1.99