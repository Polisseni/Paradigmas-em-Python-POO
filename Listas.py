num = [2, 5, 9, 1]
num [2] = 3   # O terceiro elemento passará de 9 a valer 3; listas são totalmente mutaveis
#num [4] = 7  # Nao se adiciona valores a listas dessa forma
num.append(7)
num.sort(reverse=True)   # Do maior para o menor valor da lista
num.insert(2, 0)   # Na posição 2 será inserido o valor 0
#num.pop(2)   # Sem nenhum parâmetro eliminará o valor "1" (último)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5...')
num.remove(2)   # Eliminará a primeira ocorrência do número "2"
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):   # c = posição (0, 1, 2...) e o v = cada valor digitado na lista "valores"
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao FINAL da lista!')

# Lendo valores pelo teclado e colocando-os na lista

valores = list()
cont = 1
for cont in range (0, 5):
    valores.append(int(input('Digite um valor inteiro: ')))

for c, v in enumerate (valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao FINAL da lista!')

a = [2, 3, 4, 7]
b = a[:]   # Jogando todos os elementos de "a" para "b", sem criar ligação
#b = a   # A partir do momento em que as listas são igualadas, o Python cria uma ligação entre elas
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
