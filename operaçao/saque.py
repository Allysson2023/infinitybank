from banco import obterconta,banco

def sacar(conta: int, valor:float ) -> None:
    cliente = obterconta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print('Saque realizado com sucesso! ')
        else:
            print('Saldo insuficiente! ')
    else:
        print('Cliente nao encontrado ! ')

print(banco)
sacar(1,100)
print(banco)