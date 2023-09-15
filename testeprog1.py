menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#add infos da conta
ativo = True
saldo = 0
limite_valor = 2000
extrato = ""
numero_saques = 0
limite_saques = 5

import time
limite_valor = 2000
tempo_renovacao = 24*60*60 #renovação diaria


while ativo:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida. Valor não correspondente.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        excedeu_limite = valor > limite_valor
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_limite:
            print("Operação inválida. O valor excede o limite.")
        if excedeu_saldo:
            print("Operação inválida. Saldo insuficiente.")
        if excedeu_saques:
            print("Operação inválida. Numero maximo de saques excedido.")
        if valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor infomado é inválido")
    elif opcao == "e":
        print("\n===============EXTRATO===============")
        print("Não houveram movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")
    
    elif opcao == "q":
        print("Sessão Encerrada")
        ativo = False
    else:
        print("Operação inválida. Por favor, digite novamente a operação desejada.")