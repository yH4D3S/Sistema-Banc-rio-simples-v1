menu = """ 
Bem vindo(a) ao sistema báncario de Izaac!!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo =  0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if (opcao == "d"):
        valor_depositado = float(input('Digite um valor a ser dépositado: '))
        if (valor_depositado > 0):
            saldo += valor_depositado
            extrato = f"Você tem um total de R$ {saldo:.2f}".replace(".", ",")
            print(f"Você depósitou um total de R$ {valor_depositado:.2f}, seu saldo atual é R$ {saldo:.2f}".replace(".", ","))
        else:
                print('Operação inválida, por favor digite um número válido para déposito')
    elif (opcao == 's'):
        saque = float(input('Insira a quantia que você, deseja sacar: '))
        if (numero_saques == LIMITE_SAQUES):
            print('Você atingiu o número de saques máximos diários.')
        else:
            if ((saldo >= saque) and (saque > 0)):
                saldo -= saque
                extrato = f"Você tem um total de R$ {saldo:.2f}".replace(".", ",")
                print(f"Você sacou um total de R$ {saque:.2f}, seu saldo atual é R$ {saldo:.2f}".replace(".", ","))
                numero_saques += 1

            elif (saque > saldo):
                print('Saldo insuficiente!')

            else:
                print('Operação inválida, por favor digite um número válido para saque')
    elif(opcao == 'e'):
        print(f"Você tem um total de R$ {saldo:.2f}".replace(".", ","))
    elif (opcao == 'q'):
        break
    
    else:
        print('Operação inválida, por favor selecione uma operação válida.')