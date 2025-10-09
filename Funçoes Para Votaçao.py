def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é OPCIONAL'
    else:
        return f'Com {idade} anos o voto É OBRIGATÓRIO'


#Programa Principal
nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))
