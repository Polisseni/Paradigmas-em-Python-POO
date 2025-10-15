import datetime
from classes.Extrato import Extrato


class Conta:

    def __init__(self, clientes, numero, saldo):
        self.numero = numero
        self.clientes = clientes
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transaçoes.append(["DEPÓSITO", valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False #SALDO INSUFICIENTE
        else:
            self.saldo -= valor
            self.extrato.transaçoes.append(["SAQUE", valor, datetime.datetime.today()])

            return True #SAQUE REALIZADO COM SUCESSO

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return ("\033[31mNão existe saldo suficiente\033[m")
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transaçoes.append(["TRANSFERÊNCIA", valor, datetime.datetime.today()])

            return ("\033[34mTransferência Realizada!\033[m")

    def gerar_saldo(self):
        print(f'número: {self.numero}\nsaldo: R${self.saldo}')
