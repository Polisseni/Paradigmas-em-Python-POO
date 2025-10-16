class Poupança:

    def __init__(self, taxa_remuneraçao):
        self.taxa_remuneraçao = taxa_remuneraçao

    def remuneraçao_Conta(self):
        self.saldo += self.saldo * self.taxa_remuneraçao
        