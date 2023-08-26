from banco import obterconta,banco

def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterconta(contaOri)
    contadestino = obterconta(contaDes)
    if contaOrigem and contadestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contadestino['saldo'] += valor
            print('Transferencia realizada com sucesso! ')
        else:
            print('Saldo insuficiente para transferencia! ')
    else:
        print('Uma ou mais contas nao encontradas! ')
print(banco)
transferir(1,2,100)
print(banco)