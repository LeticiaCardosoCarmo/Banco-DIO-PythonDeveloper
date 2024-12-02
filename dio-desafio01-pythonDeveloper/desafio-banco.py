saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    valor = float(input("Digite o valor que deseja depositar: "))
    if valor < 0:
        print("Você deve digitar um valor válido. Digite um valor positivo")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def sacar():
    global saldo, numero_saques, extrato, LIMITE_SAQUES
    valor = float(input("Digite o valor que deseja sacar: "))
    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saques = numero_saques >= LIMITE_SAQUES
    if execedeu_saldo:
        print("Operação falhou por não ter saldo suficiente.")
    elif execedeu_limite:
        print("Operação falhou por ter excedido o limite de R$500.00 de saque.")
    elif execedeu_saques:
        print("Operação falhou por ter excedido o limite de 03 saques diários.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        numero_saques += 1        
    else:
        print("Valor de saque inválido!!")

def mostrar_extrato():
    global saldo, extrato
    print("\n#### EXTRATO ####")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}\n")
    print("====================")

def menu():
    print("#### MENU ####")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")

while True:
    menu()
    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        depositar()   
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        mostrar_extrato()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, digite uma opção válida.")
