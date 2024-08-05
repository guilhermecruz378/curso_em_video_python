matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
csom = par = lsom =  0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l},{c}] '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print('\n')
print('-='*30)
print(f'A soma total é {par}')
print('-='*30)
for l in range(0, 3):
    lsom += matriz[1][l]
print(f'a soma da segunda linha é {lsom}')
print('-='*30)
for c in range(0, 3):
    csom += matriz[c][2]
print(f'A soma da terceira coluna é {csom}')