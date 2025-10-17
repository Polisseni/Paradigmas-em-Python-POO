larg = float(input('Digite a largura da parede (em metros): '))
alt = float(input('Digite a altura da parede (em metros): '))
area = larg * alt
print(f'Sua parede tem a dimensão {larg} x {alt} e uma área de {area:.3f}m².')
tinta = area / 2
print(f'Para pintar essa parede de {area}m² serão necessários {tinta:.3f}L de tinta.')
