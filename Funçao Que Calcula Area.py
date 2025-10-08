def area(larg, comp):
    a = larg * comp
    print(f'Um terreno {larg} x {comp} tem {a}m².')


print('CONTROLE DE TERRENOS')
print('-' * 30)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)
