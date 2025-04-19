# Sistema Bancário Simples

# Premissas #
# --- Versão 1.0 ---
# - O sistema deve permitir depósitos, saques e extratos. [OK]
# - O sistema deve validar os valores de depósito e saque. [OK]
# - O sistema deve limitar o número de saques por dia (3 saques) [OK]
# - O Sistema deve permitir saques de até R$ 500,00 por operação. [OK]
# - O sistema deve exibir um extrato com os últimos saques e depósitos. [OK]
# - O sistema deve permitir o encerramento do programa. [OK]
 
  
menu = """=== Sistema Bancário ===

[1] - Depósito 
[2] - Saque 
[3] - Extrato 
[0] - Sair

Escolha uma opção: """	

#print(menu)

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0



while True:

    opcao = input(menu)

### Depósito ###
    if opcao == "1":
        print("\nVocê selecionou: Depósito")
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}.")
            print(f"você depositou R$ {valor:.2f}, teu saldo é de R$ {saldo:.2f}.")

        else:
            print("Valor inválido, tente novamente.")


### Saque ###
    elif opcao == "2":
        print("\nVocê selecionou: Saque")
        valor = float(input("Digite o valor do saque: "))

        if numero_saques > LIMITE_SAQUES:
            print("Número de saques excedido (3 saques por dia).")

        elif valor > 500:
            print("Valor de saque superior a R$ 500,00")

        elif valor > 0 and valor <= saldo and valor < 500:
            saldo -= valor
            extrato.append(f"Saque: -R$ {valor:.2f}.")
            numero_saques += numero_saques
            print(f"Você efetuou o saque de R$ {valor:.2f}, teu saldo é de R$ {saldo:.2f}.")

        elif valor > saldo:
            print(f"sem limite para esta transação. Teu saldo é de R$ {saldo:.2f}.")

        else:
            print("Valor inválido, tente novamente.")


### Extrato ###
    elif opcao == "3":
        print("\nVocê selecionou: Extrato")
        if extrato:
            print("\n".join(extrato))
            print(f"Teu saldo é de R$ {saldo:.2f}")
        else:
            print("Não há movimentações.")


### Sair ###
    elif opcao == "0":
        print("\nSaindo do sistema. Até logo!")
        break
    
    else:
        print("\nFunção inválida. Tente novamente.")
