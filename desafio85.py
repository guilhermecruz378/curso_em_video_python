'''par = list()
impar = list()
colhedor = list()
for vans in range(1, 7):
    colhedor.append(int(input(f'Digite o {vans}º valor inteiro: ')))
    if colhedor[0] % 2 == 0:
        par.append(colhedor[:])
    elif colhedor[0] % 2 != 0:
        impar.append(colhedor[:])
    colhedor.clear()
print(f'Os números pares são {sorted(par)}')
print(f'Os números impares são {sorted(impar)}')'''
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor na posição: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valoes pares digitados são {num[0]}')
print(f'Os valores impares digitados são {num[1]}')