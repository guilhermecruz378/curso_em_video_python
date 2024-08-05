#sorteando numeros e colocando em tuplas
from random import randint
numeros = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
for c in numeros: #Para cada elementos dentro da minha variavel...
    print(c, end=' ')
print(f'\nO maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')

