lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print('-='*30)
print(lista)
print(f'Foram digitados {len(lista)} elementos...')
lista.sort(reverse = True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 ESTÁ na lista!')
else:
    print('O valor 5 NÃO está na lista!')