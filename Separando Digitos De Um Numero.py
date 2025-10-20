num = int(input('Digite um número[limite/9999]: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando número {num}...')
print(f'UNIDADE: {u}')
print(f'DEZENA: {d}')
print(f'CENTENA: {c}')
print(f'MILHAR: {m}')
