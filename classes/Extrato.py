class Extrato:

    def __init__(self):
        self.transaçoes = []

    def gerar_extrato(self, conta):
        print(f"\033[34mExtrato da conta {conta}\033[m")
        for tran in self.transaçoes:
            print(f"{tran[0]:15s} {tran[1]:12.2f} {tran[2].strftime('%d/%b/%Y')}")

        print(f"SALDO ATUAL:R${conta.saldo:12.2f} \n")


# [0 - Tipo 1 - Tipo 2 - Data]