s = 0
i = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num
        i += 1
print(f'Você informou {i} números pares e a soma é {s}')
