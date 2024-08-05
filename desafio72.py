numeral = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usuario = int(input('Digite um número entre 0 e 20: '))
    if 0 <= usuario <= 20 :
        print(f'Você digitou o número {numeral[usuario]}')
    else:
        print('TENTE NOVAMENTE.',end='')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? ').strip().upper()[0]
    if continuar == 'S':
        usuario = ' '
    else:
        break
print('FIM DO PROGRAMA!!!')