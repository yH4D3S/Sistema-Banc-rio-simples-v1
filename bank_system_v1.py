menu = """ 
Bem vindo(a) ao sistema báncario de Izaac!!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo =  0
limite = 500
limite_usado = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if (opcao == "d"):
        valor_depositado = float(input('Digite um valor a ser dépositado: '))
        if (valor_depositado > 0):
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
            print(f"Você depósitou um total de R$ {valor_depositado:.2f}, seu saldo atual é R$ {saldo:.2f}".replace(".", ","))
        else:
                print('Operação inválida, por favor digite um número válido para déposito')
    elif (opcao == 's'):

        saque = float(input('Insira a quantia que você, deseja sacar: '))

        if (numero_saques == LIMITE_SAQUES):
            print('Você atingiu o número de saques máximos diários.')
        else:
            
            if ((saldo >= saque) and (saque > 0) and (limite_usado + saque) <= limite):
                saldo -= saque
                limite_usado += saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                print(f"Você sacou um total de R$ {saque:.2f}, seu saldo atual é R$ {saldo:.2f}".replace(".", ","))
                numero_saques += 1

            elif (saque > saldo):

                print('Saldo insuficiente!')

            elif (limite_usado >= limite): 
                print("Você excedeu antigiu o limite de quantia retirada diária.")

            else:
                print('Operação inválida, por favor digite um número válido para saque')
    elif(opcao == 'e'):
        print(extrato + f"\nVocê tem um total de R$ {saldo:.2f}".replace(".", ","))
    elif (opcao == 'q'):
        break
    
    else:
        print('Operação inválida, por favor selecione uma operação válida.')
