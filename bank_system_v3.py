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
            return clientes
    print("✅ CPF válido! Continuando cadastro...")
    

    nome = input("Digite seu nome completo: ")

    data_nascimento = input("Digite sua data de nascimento(XX/XX/XXXX): ")

    print("\n=== Endereço ===")
    logradouro = input("Digite o logradouro (rua, avenida, etc.): ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    sigla_estado = input("Digite a sigla do estado (ex: SP, RJ): ").upper()
    
    endereco = f"{logradouro} - {numero} - {bairro} - {cidade} / {sigla_estado}"

    cliente = {
        "cpf": cpf,
        "nome": nome,
        "endereco": endereco,
        "data_nascimento": data_nascimento
    }

    clientes.append(cliente)
    
    print("Cliente cadastrado com sucesso!")
    return clientes

def criar_conta(clientes, contas, numero_conta_atual):
    cpf = input('Digite seu CPF: ')

    cliente_encontrado = False # Flag começa como false

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            cliente_encontrado = True # Ao encontrar o cliente, a bandeira é marcada, a criação de conta segue normalmente
            conta = {
                "cpf": cpf,
                "numero da conta": numero_conta_atual,
                "agência": "0001",
                "saldo": 0,
                "extrato": "",
            }
            contas.append(conta)
            numero_conta_atual += 1
            break # Para o Loop

    if cliente_encontrado:
        print('Conta criada com sucesso!')
        return contas, numero_conta_atual
    else:
        print("Usuário não detectado, retornando ao menu.")
        return contas, numero_conta_atual

menu = """ 
Bem vindo(a) ao sistema bancário de Izaac!!

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastro
[cc] Cadastrar Conta
[q] Sair

=> """

saldo =  0
limite = 500
limite_usado = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = []
contas = []
numero_conta_atual = 1


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

    elif (opcao == 'cc'):
        contas, numero_conta_atual = criar_conta(clientes, contas, numero_conta_atual)
    elif (opcao == 'q'):
        break
    
    else:
        print('Operação inválida, por favor selecione uma operação válida.')
