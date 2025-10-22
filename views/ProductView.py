from rich.console import Console
from rich.table import Table

class ProdutoView:

    @staticmethod
    def mostrarProdutos(produtos):
        console = Console()

        table = Table(title="Lista de produtos", show_header=True, header_style="bold magenta")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Nome", style="green")
        table.add_column("Quantidade", justify="right", style="yellow")
        table.add_column("Preço", style="blue" )

        for produto in produtos:
            table.add_row(
                str(produto.id),
                produto.nome,
                str(produto.quantidade),
                f"R${produto.preco:.2f}"
            )
        
        console.print(table)