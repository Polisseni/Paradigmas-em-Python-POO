#CADA DEF ABAIXO COMO SE FOSSE UM MODULO
#from modulos import moeda
from time import sleep


def aumentar(preço = 0, taxa = 0):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço = 0, taxa = 0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço = 0):
    res = preço * 2
    return res


def metade(preço = 0):
    res = preço / 2
    return res


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço}'.replace('.',',')


#Programa Principal
p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${metade(p):.2f}.')
sleep(0.5)
print(f'O dobro de R${p:.2f} é R${dobro(p):.2f}.')
sleep(0.5)
print(f'Aumentando R${p:.2f} em 10% o novo valor será de R${aumentar(p, 10):.2f}.')
sleep(0.5)
print(f'Diminuindo R${p:.2f} em 20% o novo valor será de R${diminuir(p, 20):.2f}')


