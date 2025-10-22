valores = list()
while True:
    numeros = (int(input('Digite um valor inteiro: ')))
    if numeros not in valores:
        valores.append(numeros)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não foi adicionado a lista...')

    resposta = str(input('Quer continuar?[S/N]: '))
    if resposta in 'Nn':
        break
valores.sort()
print('-=' * 30)
print(f'Os valores digitados em ordem crescente foram: {valores}')
