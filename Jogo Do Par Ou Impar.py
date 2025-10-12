from random import randint
v = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(0, 10)
    total = n + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR[P/I]?: ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador jogou {pc}. Total de {total}.')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!!')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!!')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos JOGAR novamente...')
print(f'GAME OVER! Você venceu {v} vezes!')
