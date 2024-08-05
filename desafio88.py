from random import randint
from time import sleep
'''mega = [0, 0, 0, 0, 0, 0]
print('-='*30)
print(f'{'JOGA NA MEGA SENA':^10}')
print('-='*30)
quant = int(input('quantos jogos você quer que eu sorteie? '))
print('-='*3, f'Sorteado {quant} jogos', '-='*3)
sleep(1)
for c in range(1, quant+1):
    mega = randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)
    print(f'Jogo {c}: {sorted(mega[:])}')
    sleep(1)
print('-='*5, '> BOA SORTE <', '-='*5)'''

lista = list()
jogos = list()
print('-='*30)
print(f'{'JOGA NA MEGA SENA':^10}')
print('-='*30)
quant = int(input('quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'Sorteado {quant} jogos', '-='*3)
sleep(1)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)