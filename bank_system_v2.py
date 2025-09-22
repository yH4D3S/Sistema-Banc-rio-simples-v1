# Funções de comando

def depositar(saldo, extrato, /):

    valor_depositado = float(input('Digite um valor a ser dépositado: '))
    if (valor_depositado > 0):
        saldo += valor_depositado
        extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        print(f"Você depósitou um total de R$ {valor_depositado:.2f}, seu saldo atual é R$ {saldo:.2f}".replace(".", ","))
    else:
        print('Operação inválida, por favor digite um número válido para déposito')
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_usado):
    saque = float(input('Insira a quantia que você, deseja sacar: '))

    if (numero_saques == LIMITE_SAQUES):
            print('Você atingiu o número de saques máximos diários.')
    else:
            
        if ((saldo >= saque) and (saque > 0) and (limite_usado + saque) <= limite):

            saldo -= saque
            limite_usado += saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print(f"Você sacou um total de R$ {saque:.2f}, seu saldo atual é R$ {saldo:.2f}".replace(".", ","))

        elif (saque > saldo):

            print('Saldo insuficiente!')

        elif ((limite_usado + saque) > limite): 
            print("Você excedeu o limite de quantia retirada diária.")
        else:
            print('Operação inválida, por favor digite um número válido para saque.')
    return saldo, extrato, numero_saques, limite_usado

def mostrar_extrato(saldo, /, *, extrato):
    print(extrato + f"\nVocê tem um total de R$ {saldo:.2f}".replace(".", ","))

def criar_cliente(clientes):
    print("== Cadastro de Cliente ===")

    cpf = input("Digite o CPF(Somente números): ")

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Erro: CPF já cadastrado")
    print("✅ CPF válido! Continuando cadastro...")
    

    nome = input("Digite seu nome completo:")

    data_nascimento = input("Digite sua data de nascimento(XX/XX/XXXX): ")

    endereco = input("Digite seu endereço: ")

    cliente = {
        "cpf": cpf,
        "nome": nome,
        "endereco": endereco,
        "data_nascimento": data_nascimento
    }

    clientes.append(cliente)
    
    print("Cliente cadastrado com sucesso!")
    return clientes


menu = """ 
Bem vindo(a) ao sistema bancário de Izaac!!

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastro
[q] Sair

=> """

saldo =  0
limite = 500
limite_usado = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = []

while True:
    
    opcao = input(menu)
    
    if (opcao == "d"):
        saldo, extrato = depositar(saldo, extrato)

    elif (opcao == 's'):
        saldo, extrato, numero_saques, limite_usado = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_usado=limite_usado)

    elif(opcao == 'e'):
       mostrar_extrato(saldo, extrato=extrato)

    elif(opcao == "c"):
        clientes = criar_cliente(clientes)
    elif (opcao == 'q'):
        break
    
    else:
        print('Operação inválida, por favor selecione uma operação válida.')
