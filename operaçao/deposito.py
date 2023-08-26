from banco import obterconta,banco
def deposito(conta: int,valor: float) -> None:
    cliente = obterconta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('Deposito realizado com sucesso! ')
    else:
        print('Cliente nao encontrado! ')

print(banco)
deposito(1,200)
print(banco)