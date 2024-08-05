'''
não previso de comtador para contar os cadstros posso usar o len
para ver o menor e o maior eu crio uma variavel para cada com zero
logo apos eu uso o if com essas variaveis para indicar qual o menor e o maior nas listas 
usando o fatiamnento no if
crio um for c in lista para ele varrer a lista toda dps uso um if no fatiamento para ver qual deve mostrar if c[1] == maior: -> 
print(c[0]) . assim tambem para o menor
'''

lista = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso Kg: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    quer = ' '
    while quer[0] not in 'NnSs':
        quer = input('Quer continuar? ')
    if quer in 'Nn':
        break

print(lista)
print(f'{len(lista)} Foram cadastradas... ')
print(f'O mais pesado é {maior}',end=' ')
for ma in lista:
    if ma[1] == maior:
        print(ma[0],end=' ')
print(f'\nO mais leve é {menor}',end=' ')
for me in lista:
    if me[1] == menor:
        print(me[0],end=' ')