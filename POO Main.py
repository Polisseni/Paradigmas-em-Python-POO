from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.Conta_Especial import ContaEspecial
from classes.Conta_Remunerada_Da_Poupança import Conta_Remunerada_Poupança


cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("321", "Maria", "Rua Y")
cliente3 = Cliente("456", "Zezinho", "Rua Z")

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = Conta_Remunerada_Poupança(cliente3, 3, 2000, 0.1)

conta2.depositar(800)

conta2.gerar_saldo()
conta3.gerar_saldo()

'''conta3 = ContaEspecial(cliente3, 3, 2000, 1000)

conta1.depositar(300)
conta1.transfere_valor(conta2, 500)
conta2.sacar(700)
conta3.depositar(800)
conta3.sacar(4000)

conta1.extrato.gerar_extrato(conta1)
conta2.extrato.gerar_extrato(conta2)
conta3.extrato.gerar_extrato(conta3)'''
