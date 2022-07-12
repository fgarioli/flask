Elabore um sistema de compras. Este sistema deve tratar de adicionar produtos, e calcular o valor final de uma compra, dado o nome de um produto e a quantidade comprada. Neste sistema é possível apenas comprar uma variedade de produto por compra. Para tal você deverá seguir os seguintes passos:
 - De cada produto devem ser recebidos os seguintes dados:
    - nome
    - preço unitário. 
 - A forma de armazenamento escolhida para estes dados deve utilizar listas (nomes, precos). Observe a tabela de listas abaixo:  

    | nomes    | preços     |
    | -------- | ---------- |
    | Sandália | R$ 49,90   |
    | Camisa   | R$ 79,90   |
    | Calça    | R$ 109,90  |

```python
opcao = 0
while opcao != 4:
    print("SISTEMA DE COMPRAS")
    print("1 - Adicionar Produto")
    print("2 - Consultar Preço Produto")
    print("3 - Calcular Compra")
    print("4 - Sair")

    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        adicionarProduto()
    elif opcao == 2:
        nomeProduto = input("Digite o nome do produto: ")
        preco = consultarPrecoProduto(nomeProduto)
        print(f"O preço do produto {nomeProduto} é {preco}")
    elif opcao == 3:
        nomeProduto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        valorTotal = calcularCompra(nomeProduto, quantidade)
        print(f"O valor total da compra é: {valorTotal}")
    elif: opcao == 4:
        exit()
    else:
        print("Opção incorreta!")
```
Considerando o código acima, que você deve copiar e utilizar no seu programa exatamente como foi escrito, você deverá elaborar 1 procedimento (adicionarProduto) e 2 funções (consultarPrecoProduto e calcularCompra).

 - **adicionarProduto**: Este procedimento não deve receber nada como parâmetro. O propósito deste procedimento é ler o nome e o preço do novo produto e armazená-los respectivamente nos vetores (nomes, precos).
 - **consultarPrecoProduto**: Esta função deve receber como parâmetro o nome do produto e retornar o preço do mesmo.
 - **calcularCompra**: Esta função deve receber como parâmetros o nome do produto e a quantidade comprada, e retornar o valor total da compra da seguinte forma:
    - caso o valor total da compra, seja maior ou igual a R$100,00, adicionar 10% de imposto ao valor total.
    - caso o valor total da compra seja maior ou igual a R$50,00 e inferior a R$100,00, adicionar 12% ao valor total.
    - caso o valor total da compra seja inferior a R$50,00, adicionar 15% ao valor total.