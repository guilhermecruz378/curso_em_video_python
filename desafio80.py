# ------- LISTAS EM PYTHON SEM SORT E REPETIÇÃO ----- preciso fazer uma lista receber um número digitado pelo usuario e colocalos em uma lista ordenadamente
lista = list()
for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Número adicionado na ultima posição')
    else:
        pos = 0
        while pos <= len(lista):
            if numero < lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição: {pos}')
                break
            pos += 1
print(lista)