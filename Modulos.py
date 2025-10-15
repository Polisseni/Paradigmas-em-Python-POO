#CADA DEF ABAIXO COMO SE FOSSE UM MODULO
from time import sleep

def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res


#Programa Principal
p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${metade(p):.2f}.')
sleep(0.5)
print(f'O dobro de R${p:.2f} é R${dobro(p):.2f}.')
sleep(0.5)
print(f'Aumentando R${p:.2f} em 10% o novo valor será de R${aumentar(p, 10):.2f}.')
sleep(0.5)
print(f'Diminuindo R${p:.2f} em 20% o novo valor será de R${diminuir(p, 20):.2f}')
