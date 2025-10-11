from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
ranking = ()
print('Valores Sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print('-=' * 20)
print('   == RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'  {i+1}ºlugar: {v[0]} com {v[1]}.')
    sleep(0.5)
