# Código da Classe
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor


    def sacar(self, valor):
        if self.saldo < valor:
            return False #SALDO INSUFICIENTE
        else:
            self.saldo -= valor
            return True #SAQUE REALIZADO COM SUCESSO


    def gerarextrato(self):
        print(f'Nome: {self.nomeTitular}\nNúmero: {self.numero}\nCPF: {self.cpf}\nSaldo: R${self.saldo}')


    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("\033[31mNão existe saldo suficiente\033[m")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("\033[34mTransferência Realizada!\033[m")


'''#Código do Exemplo
c1 = Conta(1, 12344321, "Guanabara", 9000)
valor_saque = 1000
resultado_saque = c1.sacar(valor_saque)

if resultado_saque:
    print(f'\033[34mSaque de R${valor_saque} realizado com SUCESSO!!\033[m')
else:
    print(f'\033[31mSaldo INSUFICIENTE para realizar a transação!\033[m')

c1.gerarextrato()
'''

conta1 = Conta(123, 88888888, "Maria", 0)
conta2 = Conta(124, 99999999, "Pedro", 500)

print(conta2.transfereValor(conta1, 250))
conta1.gerarextrato()
conta2.gerarextrato()
