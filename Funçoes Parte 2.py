def limite():
    print('=' * 40)


limite()
def contador (i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM')


#Programa Principal
contador(2, 10, 2)
limite()
help(contador)
limite()

limite()
def somar (a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma é igual a {s}.')


#Programa Principal
somar(3, 2, 5)
limite()

limite()
def funçao():
    n1 = 8   # Variável Local
    print(f'n1 dentro vale {n1}')


n1 = 4   # Variável Global
funçao()
print(f'n1 fora vale {n1}')
limite()

limite()
def somar (a = 0, b = 0, c = 0):
    s = a + b + c
    return s   # Retorna o valor da soma as variaveis r1, r2, r3


#Programa Principal
r1 = somar(3, 4, 5)
r2 = somar(8, 7)
r3 = somar(6)

print(f'Os resultados foram: {r1}, {r2} e {r3}.')
limite()
