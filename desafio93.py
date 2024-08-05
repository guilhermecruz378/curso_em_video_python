jogador = {}
golos = []
tot = 0
jogador['jogador'] = input('Qual o nome do jogador? ')
partidas = int(input(f'Quantas partidas {jogador["jogador"]} jogou: '))
for c in range(0, partidas):
    golos.append(int(input(f'   Quantos gols fez {jogador["jogador"]} na partida {c}: ')))
#    tot += golos[c]
jogador['gols'] = golos
jogador['total'] = sum(golos)
print('-='*15)
print(jogador)
print('-='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*15)
print(f'O jogador {jogador["jogador"]} tem {partidas} partidas.')
for c, i in enumerate(jogador['gols']): #enumerate(golos)
    print(f'   => Na partida {c} ele fez {i} gols.')
print(f'O total foram {jogador["total"]} gols.')