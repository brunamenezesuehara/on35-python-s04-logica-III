def main():
    cardapio = {
        100: {"especificacao": "Cachorro Quente", "preco": 1.20},
        101: {"especificacao": "Bauru Simples", "preco": 1.30},
        102: {"especificacao": "Bauru com ovo", "preco": 1.50},
        103: {"especificacao": "Hambúrguer", "preco": 1.20},
        104: {"especificacao": "Cheeseburguer", "preco": 1.30},
        105: {"especificacao": "Refrigerante", "preco": 1.00},
    }

    total_geral = 0

    print("Cardápio:")
    for codigo, item in cardapio.items():
        print(f"{item['especificacao']:15} {codigo}  R$ {item['preco']:.2f}")

    while True:
        codigo = int(input("\nDigite o código do item (ou 0 para encerrar o pedido): "))
        if codigo == 0:
            break
        if codigo in cardapio:
            quantidade = int(input("Digite a quantidade desejada: "))
            valor_item = cardapio[codigo]["preco"] * quantidade
            total_geral += valor_item
            print(f"{cardapio[codigo]['especificacao']}: {quantidade} x R$ {cardapio[codigo]['preco']:.2f} = R$ {valor_item:.2f}")
        else:
            print("Código inválido. Por favor, tente novamente.")
    print(f"\nTotal geral do pedido: R$ {total_geral:.2f}")
main()
