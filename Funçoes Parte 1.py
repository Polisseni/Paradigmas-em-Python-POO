def soma(a,b):
    print(f'A={a} e B={b}')
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}')
def limite():
    print('-' * 35)

#PROGRAMA PRINCIPAL
limite()
soma(4, 7)
limite()
soma(a=7, b=22)
limite()
soma(13, 25)
limite()

limite()
def contador (* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

#PROGRAMA PRINCIPAL
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
limite()

limite()
def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1

#PROGRAMA PRINCIPAL
valores = [6, 3, 0, 9, 1, 13]
dobra(valores)
print(valores)
limite()

limite()
def soma (*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(3, 7, 9)
limite()
