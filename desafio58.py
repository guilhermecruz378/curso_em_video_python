from random import randint
'''
# EU--------------------=======
from time import sleep

tot = 1
pc = randint(0, 10)

print('\033[;31;40m VAMOS \033[;32;40m JOGAR! \033[m ')
sleep(1)
jogador = int(input('De 0 a 10 adivinhe o número que pensei: '))
while pc != jogador:
    if pc > jogador:
        print('MAIS...', end='')
    elif pc < jogador:
        print('MENOS...', end='')
    print('\033[;31;40m ERROU\033[m, tente mais uma vez! ')
    sleep(1)
    jogador = int(input('De 0 a 10 adivinhe o número que pensei: '))
    tot += 1
print(f'Você \033[;32;40m ACERTOU \033[m você precisou de \033[;32;40m{tot}\033[m tentativas ')'''

# PROFESSOR -----------------------====

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Você consegue adivinhar qual foi? ')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador: 
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns')