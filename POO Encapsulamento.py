from classes.ContaEncapsulamentoAula import Conta


c1 = Conta(1, 1000)
c2 = Conta(2, 50)
c3 = Conta(3, 500)
c1.sacar(200)
c1.saldo = 1500

print(f"Até agora temos {Conta.get_total_contas()} conta(s) criadas.")
print(f'Muito obrigado por ser cliente do {Conta.nome_do_banco()}!')

#c1._Conta__saldo = -8000   # MUDANDO ATRIBUTO PRIVADO PARA PÚBLICO / HACKER
#print(f"Conta 1 com R${c1.__saldo}")
#print(f"Conta 2 com R${c2.__saldo}")
c1.gerar_saldo()
c2.gerar_saldo()
