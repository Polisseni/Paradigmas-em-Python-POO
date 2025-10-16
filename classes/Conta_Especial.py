from classes.Conta import Conta
import datetime


class ContaEspecial(Conta):

    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            print(f'\033[31mNão existe saldo suficiente!\033[m Conta número {self.numero} e cliente {self.clientes.cpf}')
            return False  # SALDO INSUFICIENTE
        else:
            self.saldo -= valor
            if self.saldo < 0:
                self.limite += self.saldo
            self.extrato.transaçoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True  # SAQUE REALIZADO COM SUCESSO
