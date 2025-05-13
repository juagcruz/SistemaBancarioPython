# Sistema Bancário Simples

# Premissas #
# --- Versão 2.0 ---
# - O sistema deve permitir depósitos, saques e extratos. [OK]
# - O sistema deve validar os valores de depósito e saque. [OK]
# - O sistema deve limitar o número de saques por dia (3 saques) [OK]
# - O Sistema deve permitir saques de até R$ 500,00 por operação. [OK]
# - O sistema deve exibir um extrato com os últimos saques e depósitos. [OK]
# - O sistema deve permitir o encerramento do programa. [OK]
#
 
  
from datetime import datetime



data_hj = datetime.now()
data_hj_ = data_hj.strftime("%Y-%m-%d %H:%M:%S //")
LIMITE_SAQUES = 3
AGENCIA = "0001"




def menu():

    menu = """=== Sistema Bancário ===

    [1] - Depósito 
    [2] - Saque 
    [3] - Extrato
    [4] - Criar Usuario
    [5] - Criar Conta 
    [6] - Listar Contas
    [0] - Sair

    Escolha uma opção: """

    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"{data_hj_}: Depósito: R$ {valor:.2f}.")
        print(f"{data_hj_}: você depositou R$ {valor:.2f}, teu saldo é de R$ {saldo:.2f}.")

    else:
        print("Valor inválido, tente novamente.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if numero_saques > LIMITE_SAQUES:
        print(f"{data_hj_}: Número de saques excedido (3 saques por dia).")

    elif valor > 500:
        print(f"{data_hj_}: Valor de saque superior a R$ 500,00")

    elif valor > 0 and valor <= saldo and valor < 500:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}.")
        numero_saques += 1
        print(f"{data_hj_}: Você efetuou o saque de R$ {valor:.2f}, teu saldo é de R$ {saldo:.2f}.")

    elif valor > saldo:
        print(f"{data_hj_}: sem limite para esta transação. Teu saldo é de R$ {saldo:.2f}.")

    else:
        print(f"{data_hj_}: Valor inválido, tente novamente.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    if extrato:
        print("\n".join(extrato))
        print(f"{data_hj_}: Teu saldo é de R$ {saldo:.2f}")
    else:
        print(f"{data_hj_}: Não há movimentações.")

    return saldo, extrato    

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com este CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, criação encerrada! ")

def listar_contas(contas):
    for conta in contas:
        print(f"""
            Agencia: {conta['agencia']}
            C/C:   {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
              """)

def main():

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    valor = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

### Depósito ###
        if opcao == "1":

            print("\nVocê selecionou: Depósito")
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

    ### Saque ###
        elif opcao == "2":
            print("\nVocê selecionou: Saque")
            valor = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(
                  saldo=saldo,
                  valor=valor,
                  extrato=extrato,
                  limite=limite,
                  numero_saques=numero_saques,
                  limite_saques=LIMITE_SAQUES,
            )

    ### Extrato ###
        elif opcao == "3":
            print("\nVocê selecionou: Extrato")
            exibir_extrato(saldo, extrato=extrato)
        
    ### Cria usuário ###
        elif opcao == "4":
            print("\nVocê selecionou: Criar Usuário")
            criar_usuario(usuarios)

    ### Cria Conta ###
        elif opcao == "5":
            print("\nVocê selecionou: Criar Conta")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

    ### Sair ###
        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break
        
        else:
            print("\nFunção inválida. Tente novamente.")

main()