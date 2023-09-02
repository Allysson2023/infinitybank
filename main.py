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

---------------------------------------------------------------------------------------------------
from  tkinter import*
from tkinter import messagebox

def calcularImc() -> None:
    peso = float(txt_peso.get())
    altura = float(txt_altura.get())
    imc = peso/ altura **2
    messagebox.showinfo("Resultado!",f"Seu imc é:{imc:.2f}")
    txt_peso.delete(0, END)
    txt_altura.delete(0,END)


janela = Tk()
#como colocar um titulo na janela
janela.title("Primeira janela")
#como modificar o tamanho
janela.geometry("350x300")

label_peso = Label(janela,
                   text="Peso: ",
                   fg="red",
                   font="Arial 14 bold")

label_altura = Label(janela,
                   text="Altura: ",
                   fg="red",
                   font="Arial 14 bold")

txt_peso = Entry(janela, font="Arial 13")
txt_altura = Entry(janela, font="Arial 13")

btn_calcular = Button(janela, text="calcular", fg="blue", width=8,height=1,font="Arial 14 bold", bg="yellow",command=calcularImc)
btn_calcular.grid(row=2, column=0)





txt_peso.grid(row=0, column=1)
txt_altura.grid(row=1, column=1)



label_peso.grid(row=0, column=0)

label_altura.grid(row=1, column=0)

janela.mainloop()
