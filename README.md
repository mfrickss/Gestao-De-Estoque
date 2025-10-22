# Gestão de Estoque

Um sistema de gerenciamento de estoque desenvolvido em **Python**, que permite ao usuário **adicionar, remover, atualizar e listar produtos**, além de **salvar dados em JSON** e **exportar relatórios em CSV**.  
O projeto foi estruturado com foco em **organização, modularização e facilidade de manutenção**.

---

## 📋 Descrição

Este sistema realiza o controle completo de produtos em estoque por meio de um menu interativo no console.  
É possível visualizar todos os produtos cadastrados, modificar quantidades, alterar preços e remover itens quando necessário.  
Os dados são persistidos em um arquivo JSON e podem ser exportados para CSV, permitindo a integração com outras ferramentas.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Python 3+**
- **Programação Orientada a Objetos (POO)**
- **Manipulação de Arquivos JSON e CSV**
- **Testes Automatizados com Pytest**
- **Organização Modular**
- **Boas Práticas de Estrutura e Legibilidade de Código**

---

## 📁 Estrutura do Projeto
          
```
gestao-de-estoque/
├── .gitignore                    # Arquivo de ignorados do Git (configurações, caches, etc.)
├── estoque.json                  # Armazena os dados persistidos do estoque
├── main.py                       # Ponto de entrada da aplicação
├── meuEstoque.csv                # Exportação dos produtos em formato CSV
├── factories/                    # Módulos para criação de objetos
│ └── produto_factory.py          # Lógica para calcular o ID e criar novos produtos
├── models/                       # Módulos responsáveis pelas classes de domínio
│ ├── init.py
│ ├── estoque.py                  # Classe Estoque (gerencia operações do inventário)
│ └── produto.py                  # Classe Produto (representa um item do estoque)
├── repositories/                 # Módulos para persistência e acesso a dados
│ └── estoque_repository.py       # Lida com a leitura/escrita de JSON e exportação de CSV
├── views/
│ └── ProductView.py              # Formata a tabela dos produtos
├── tests/                        # Testes automatizados
│ └── test_estoque.py
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação do sistema
```


---

## 🚀 Como Executar

1. **Clone o repositório:**
```bash
git clone https://github.com/mfrickss/Gestao-De-Estoque
```

2. Acesse o diretório do projeto:
```bash
cd gestao-de-estoque
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4.Execute a aplicação:
```bash
python main.py
```

O sistema exibirá um menu no terminal com todas as opções disponíveis para o gerenciamento do estoque.

---

## 🧪 Testes

Para garantir o correto funcionamento do sistema, execute os testes automatizados com:
```bash
pytest
```

Isso validará todas as principais funcionalidades da classe Estoque.

---

## 👨‍💻 Autor

- [Ricardo Camargo](https://github.com/mfrickss)

---

## 📄 Licença

Este projeto é livre para uso acadêmico e de estudo, podendo ser adaptado conforme as necessidades do desenvolvedor.

