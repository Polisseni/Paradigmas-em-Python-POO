from classes.Conta import Conta
from classes.Poupança import Poupança


class Conta_Remunerada_Poupança(Conta, Poupança):

    def __init__(self, clientes, numero, saldo, taxa_remuneração):
        Conta.__init__(self, clientes, numero, saldo)
        Poupança.__init__(self, taxa_remuneração)

    def remunera_Conta(self):
        self.saldo += self.saldo * (self.taxa_remuneraçao / 30)

