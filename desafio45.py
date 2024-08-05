from random import randint
from time import sleep

print('Vamos jogar JOKENPÔ')
print(''' DESAFIE A MAQUINA ESCOLHA ENTRE!
      PEDRA - Digite: [0]
      PAPEL - Digite: [1]
      TESOURA - Digite: [2] ''')
jogador = input('Qual sua jogada: ')
jogador_int = int(jogador)

maquina = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)



if maquina == 0:
    if jogador_int == 0:
        print('\033[0;33;40m EMPATE! \033[m')
    elif jogador_int == 1:
        print('\033[0;32;40m vitoria \033[m')
    elif jogador_int == 2:
        print('\033[0;31;40m DERROTA! \033[m')

elif maquina == 1:
    if jogador_int == 0:
        print('\033[0;31;40m DERROTA! \033[m')
    elif jogador_int == 1:
        print('\033[0;33;40m EMPATE! \033[m')
    elif jogador_int == 2:
        print('\033[0;32;40m vitoria \033[m')

elif jogador_int == 2 :
    if jogador_int == 0:
        print('\033[0;32;40m vitoria \033[m')
    elif jogador_int == 1:
        print('\033[0;31;40m DERROTA! \033[m')
    elif jogador_int == 2:
        print('\033[0;33;40m EMPATE! \033[m')

    
else:
    print('Opção inválida')