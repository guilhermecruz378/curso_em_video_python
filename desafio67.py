#Tabuada usando flag/break
while True:
    num = int(input('Digite um número para obter sua tabuada: '))
    for c in range (0,11):
        vezes = num * c
        print(f'{num}x{c}={vezes}')
    d = input('Deseja continuar? [S/N]').strip().upper()[0]
    if d == 'N':
        break
print('FIM...')
