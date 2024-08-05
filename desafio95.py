"""jogador = {}
quant = list()
seleção = []
while True:
    jogador.clear()
    quant.clear()
    partidas = 0
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas+1):
        quant.append(int(input(f'Quantos gols na partidas {c}: ')))
    jogador['gols'] = quant[:]
    seleção.append(jogador.copy())
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? ')
    if continuar in 'Nn':
        break
print('-='*30)
print(f'{"cod":<5}{"nome":>5}{"gols":>16}{"total":>16}')
print('-'*40)
for c, i in enumerate(seleção):
    print(f'{c:<5} {i['nome']:>5} {' ':>8} {i["gols"]} {sum(i['gols']):>16}')
print('-'*40)
while True:
    mostrar = int(input('Mostrar dados de qual jogador [999 para parar: ]'))
    if mostrar == 999:
        break
    else:
        print(f'MOSTRAR DADOS DO JOGADOR -> {seleção[mostrar]["nome"]}')
        for k, i in enumerate(seleção[mostrar]['gols']):
            print(f'No {k}º jogo ele fez {i} gols')
    print('-'*40)"""

''' ----RESOLUÇÃO DO PROFESSOR----'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input(f'Quer continuar? [S/N] ')).upper()[0]
        if resp in 'N':
            break
        print('ERRO! responda apenas "S" ou "N" ')
    if resp == 'N':
        break
print('-'*40)
print('cod', end=' ') # para ficar em formato de coluna foi digitado uma string 'cod' porque não existe essa chave no dicionario
for i in jogador.keys(): #aqui está pegando as chaves do dicionario para colocar em formato de coluna
    print(f'{i:<15}', end=' ')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ') #numero do contador
    for d in v.values(): # mostrara o valor aonde o contador está indicando na lista > 0 == 'nome':'guilherme'
        print(f'{str(d):<15}', end=' ') # foi trasformado tudo em str para ser possivel colocar os acrescimos a direita.
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Não existe jogados com o código {busca}')
    else:
        print(f' -- Levantamendo do jogador {time[busca]['nome']}')
        for i, g in enumerate(time[busca]['gols']): # o laço feito para mostrar o i== indice da lista e o g == valor da lista em time[busca]['gols']
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('<< VOLTE SEMPRE >>')
