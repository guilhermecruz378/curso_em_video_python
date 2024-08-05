# Descobrindo os númros primos
number = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, number+1):
    if number % c == 0:
        print(f'\033[0;33;40m {c} \033[m', end=' ')
        tot += 1 
    else:
        print(f'\033[0;31;40m {c} \033[m', end=" ")
if tot == 2:        
    print(f'\n O número {number} foi dividido {tot} vezes por isso ele É PRIMO')
else:
    print(f'\n O número {number} foi dividido {tot} vezes por isso não é primo')


