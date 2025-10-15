class Conta:

    __total_contas = 0

    @classmethod
    def get_total_contas(cls):
        return cls.__total_contas

    @staticmethod
    def nome_do_banco():
        return "Banco Guanabara"

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        type(self).__total_contas += 1

    @property   # ACESSA O ATRIBUTO SEM NECESSARIAMENTE MEXER NELE
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):  # MEXE NO SALDO E PROTEGE PRA QUE ELE NÃO FIQUE NEGATIVO!
        if valor <0:
            print('\033[31mSALDO INVÁLIDO!\033[m')
        else:
            self.__saldo = valor

    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            return True

    def gerar_saldo(self):
        print(f"Conta: {self.__numero}")
        print(f"Saldo: R${self.__saldo:10.2f}")
