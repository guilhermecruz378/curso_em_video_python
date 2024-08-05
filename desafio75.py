'''num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite mais um número: '))
tupla = (num1, num2, num3, num4)
divisor = 0'''
tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print(f'Existem apenas {tupla.count(9)} unidades de 9 nas tuplas')
if 3 in tupla: # se 3 estiver dentro da tupla:
    print(f'O número três está na {tupla.index(3)+1}ª Posição')
print('Os valores pares são: ', end='')
for c in tupla:
    if c % 2 == 0: 
        print(c, end=" ")
