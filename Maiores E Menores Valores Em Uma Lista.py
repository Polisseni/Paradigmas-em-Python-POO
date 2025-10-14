valores = list()
maior = 0
menor = 0
for cont in range (0, 5):
    valores.append(int(input(f'Digite um valor inteiro na posição {cont}: ')))
    if cont == 0:   # Quando o primeiro valor for digitado, ele é o maior e o menor ao mesmo tempo
        menor = maior = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('-=' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi o {maior} nas posições: ',end=' ')
for i, v in enumerate (valores):
    if v == maior:
        print(f'{i}... ', end =' ')
print()
print(f'O menor valor digitado foi o {menor} nas posições:  ', end=' ')
for i,v in enumerate (valores):
    if v == menor:
        print(f'{i}...', end=' ')
print()
print('-=' * 30)
