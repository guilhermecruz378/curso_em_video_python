from random import randint
from time import sleep
from operator import itemgetter
dicio = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 
         'jogador3':randint(1,6), 'jogador4':randint(1,6)}
ranking = []
print('Valores Sorteados:')
for k, v in dicio.items():
    print(f' - o {k} tirou {v} no dado. ')
    sleep(1)
print('-='*15)
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print(' == RANKING DOS JOGADORES == ')
for c, i in enumerate(ranking):
    print(f'{c+1}º Lugar: {i[0]} com {i[1]} no dado ')
    sleep(1)