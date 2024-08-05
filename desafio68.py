# jogo do par ou impar com flag
from random import randint
from time import sleep
v = 0 
while True: # estrutura de repetição laço
    jogador = int(input('Digite um número: '))
    maquina = randint(0,10)
    total = jogador + maquina
    par_ou_impar = ' '
    while par_ou_impar not in 'PI':
        par_ou_impar = input('Par ou Impar? ').strip().upper()[0]
    print(f'Você jogou {jogador} e a maquina {maquina} o total é {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    sleep(1)
    if par_ou_impar == 'P': #condição se, senao, se se 
        if total % 2 == 0:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu...')
            break
    if par_ou_impar == 'I':
        if total % 2 != 0:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu...')
            break
    print('Vamos jogar novamente...')
    sleep(1)
print(f'GAME OVER! Você venceu {v} vezes')
