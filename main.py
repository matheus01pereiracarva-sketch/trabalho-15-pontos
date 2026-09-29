# =========================================================
# TRABALHO PRÁTICO - ALGORITMOS E PROGRAMAÇÃO
# Sistema de Atendimento e Pedidos em Python
# =========================================================

def exibir_cardapio():
    """Apresenta o cardápio da lanchonete ao cliente."""
    print("\n" + "=" * 40)
    print("           CARDÁPIO DA LANCHONETE       ")
    print("=" * 40)
    print(" Código | Produto            | Preço (R$)")
    print("-" * 40)
    print("   1    | X-Burguer          | R$ 15,00")
    print("   2    | X-Salada           | R$ 18,00")
    print("   3    | Batata Frita       | R$ 12,00")
    print("   4    | Refrigerante Lata  | R$  6,00")
    print("   5    | Suco Natural       | R$  8,00")
    print("=" * 40)


def obter_preco_e_nome(codigo):
    """
    Retorna o nome e o preço do produto com base no código informado.
    Retorna None, 0.0 caso o código seja inválido.
    """
    if codigo == 1:
        return "X-Burguer", 15.00
    elif codigo == 2:
        return "X-Salada", 18.00
    elif codigo == 3:
        return "Batata Frita", 12.00
    elif codigo == 4:
        return "Refrigerante Lata", 6.00
    elif codigo == 5:
        return "Suco Natural", 8.00
    else:
        return None, 0.0


def calcular_desconto(total_compra):
    """
    Calcula a porcentagem e o valor do desconto conforme o valor total:
    - Abaixo de R$ 50,00: sem desconto (0%)
    - De R$ 50,00 até R$ 99,99: 5% de desconto
    - R$ 100,00 ou mais: 10% de desconto
    """
    if total_compra < 50.00:
        percentual = 0
    elif total_compra < 100.00:
        percentual = 5
    else:
        percentual = 10

    valor_desconto = total_compra * (percentual / 100)
    return percentual, valor_desconto


def solicitar_forma_pagamento():
    """Solicita e valida a forma de pagamento selecionada pelo cliente."""
    while True:
        print("\n--- FORMA DE PAGAMENTO ---")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
        opcao = input("Escolha a forma de pagamento (1, 2 ou 3): ").strip()

        match opcao:
            case "1":
                return "Dinheiro"
            case "2":
                return "PIX"
            case "3":
                return "Cartão"
            case _:
                print("[ERRO] Opção inválida! Por favor, escolha 1, 2 ou 3.")


def main():
    print("=" * 50)
    print("   SISTEMA DE ATENDIMENTO E REALIZAÇÃO DE PEDIDOS")
    print("=" * 50)

    # Identificação do cliente
    nome_cliente = input("Por favor, digite o seu nome: ").strip()
    while not nome_cliente:
        nome_cliente = input("O nome não pode ser vazio. Digite seu nome: ").strip()

    total_compra = 0.0
    deseja_continuar = "S"

    # Repetição dos pedidos
    while deseja_continuar.upper() == "S":
        exibir_cardapio()

        # Entrada e validação do código do produto
        codigo_input = input("Digite o código do produto desejado: ").strip()

        # Validação se a entrada é numéricas
        if not codigo_input.isdigit():
            print("[ERRO] Código inválido! Digite apenas números correspondentes aos produtos.")
            continue

        codigo = int(codigo_input)
        nome_produto, preco_unitario = obter_preco_e_nome(codigo)

        # Validação de opção inexistente
        if nome_produto is None:
            print("[ERRO] Código de produto inexistente! Tente novamente.")
            continue

        # Entrada e validação da quantidade
        qtd_input = input(f"Informe a quantidade desejada de '{nome_produto}': ").strip()
        if not qtd_input.isdigit() or int(qtd_input) <= 0:
            print("[ERRO] Quantidade inválida! Deve ser um número inteiro maior que zero.")
            continue

        quantidade = int(qtd_input)
        subtotal = preco_unitario * quantidade
        total_compra += subtotal

        print(f"-> Adicionado: {quantidade}x {nome_produto} - Subtotal: R$ {subtotal:.2f}")

        # Pergunta se deseja adicionar mais itens
        while True:
            resp = input("\nDeseja adicionar outro produto? (S/N): ").strip().upper()
            if resp == "S" or resp == "N":
                deseja_continuar = resp
                break
            else:
                print("[ERRO] Resposta inválida! Digite 'S' para Sim ou 'N' para Não.")

    # Verificação se algum item foi comprado
    if total_compra == 0.0:
        print("\nNenhum pedido foi realizado. Atendimento encerrado.")
        return

    # Cálculos das regras de desconto e pagamento
    percentual_desconto, valor_desconto = calcular_desconto(total_compra)
    valor_final = total_compra - valor_desconto
    forma_pagamento = solicitar_forma_pagamento()

    # Resumo Final do Atendimento
    print("\n" + "=" * 50)
    print("            RESUMO FINAL DO PEDIDO             ")
    print("=" * 50)
    print(f" Cliente:             {nome_cliente}")
    print(f" Valor Original:      R$ {total_compra:.2f}")
    print(f" Desconto Aplicado:   {percentual_desconto}%")
    print(f" Valor do Desconto:   R$ {valor_desconto:.2f}")
    print(f" Valor Final a Pagar: R$ {valor_final:.2f}")
    print(f" Forma de Pagamento:  {forma_pagamento}")
    print("=" * 50)
    print(" Obrigado pela preferência! Volte sempre.")


# Execução do programa
if __name__ == "__main__":
    main()