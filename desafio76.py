#Liatagem de preço
print('='*40)
print(f'{'LISTAGEM DE PREÇO':^30}')
print('='*40)
listagem = ('Lápis', 1.75, 'Caneta', 2.00,
            'Borracha', 4.25, 'Caderno', 25.80,
            'Estojo', 11.00, 'Mochila', 133.50)
for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<20}',end='') # mostrar o valor que está em tal posição
    else:
        print(f'R${listagem[posição]:.2f}')
