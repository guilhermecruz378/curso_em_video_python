#O dicionario está dentro da lista
cadastro = dict()
lista = list()
id = média = 0
while True:
    cadastro.clear()
    cadastro['nome'] = input('Nome: ')
    cadastro['sexo'] = input('Sexo: [M/F] ')
    while cadastro['sexo'] not in 'MmFf':
        print('ERRO! Responda apenas "M" ou "F".')
        cadastro['sexo'] = input('Sexo: ')
    cadastro['idade'] = int(input('idade: '))
    id += cadastro['idade']
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar not in 'SsNn':
            print('ERRO! Responda apenas "Sim" ou "Não".')
            continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    lista.append(cadastro.copy())
    if continuar in 'Nn':
        break
média = id / len(cadastro)
print('-='*15)
print(f'A) Ao todo são {len(lista)} cadastradas')
print(f'B) A média de idade é {média:.1f}')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'C) As mulheres cadastradas são {p['nome']}', end=' ')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= média:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print(' << ENCERRADO >>')