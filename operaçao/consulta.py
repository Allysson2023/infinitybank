from banco import obterconta,banco

def consultaSaldo(conta : int) -> None:
    cliente = obterconta(conta)
    if cliente:
        print(f"Seu saldo: {cliente['saldo']}")
    else:
        print('Cliente nao encontrado! ')
consultaSaldo(1)