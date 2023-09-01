from banco import obterconta,banco
from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.deposito import depositar
from operacoes.transferencia import transferir
from banco import *

def menu():
    while True:
        print("---BEM VINDO AO MENU---")
        print("1 - Adicionar conta")
        print("2 - Editar nome")
        print("3 - Consultar conta")
        print("4 - Excluir conta")
        print("5 - Listar todos")
        print("6 - Realizar saque")
        print("7 - Realizar deposito")
        print("8 - Realizar transferencia")
        print("9 - Consultar saldo")
        print("10 - Sair")
        opcao = int(input("Selecione uma opcao: "))
        if opcao == 1:
            nome = input("Digite o nome do cliente: ")
            saldo = float(input("Digite o saldo:"))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input("Digite o numero da conta:"))
            nome = input("Digite o novo nome do cliente: ")
            editarNome(conta, nome)
        elif opcao == 3:
            conta = int(input("Digite o numero da conta:"))
            buscarCliente(conta)
        elif opcao == 4:
            conta = int(input("Digite o numero da conta:"))
            removerConta(conta)
        elif opcao == 5:
            listarTodos()
        elif opcao == 6:
            conta = int(input("Digite o numero da conta:"))
            valor = float(input("Digite o valor de saque:"))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input("Digite o numero da conta:"))
            valor = float(input("Digite o valor de saque:"))
            depositar(conta, valor)
        elif opcao == 8:
            contaOrigem = int(input("Informe a conta de origem: "))
            contaDestino = int(input("Informe a conta de destino: "))
            valor = float(input("Digite o valor que deseja transferir: "))
            transferir(contaOrigem, contaDestino, valor)
        elif opcao == 9:
            conta = int(input("Digite o numero da conta:"))
            consultarSaldo(conta)
        elif opcao == 10:
            print("--- VOCE SAIU DO PROGRAMA---")
            break
        else:
            print("Opcao invalida! ")
