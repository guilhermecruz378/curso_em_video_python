'''O total deve ser maior que a cedula para haver subtração
caso não for deve ser feito a alteração da variante cedula para uma cédula menor
e o contador deve contar as cedulas ao final caso ainda tenho um total a variante contador deve retornar a zero
as cedulas serão 50, 20, 10, 1
'''
print ('='*20)
print('Bem vindo ao BANCO NOBRECRUZ')
print ('='*20)
valor = int(input('Digite qual o valor que deseja sacar: '))
total = valor
ced = 50
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced != 0:
            print(f'Saira no caixa {contced} notas de ${ced:.2f} Reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced =1
        contced = 0
        if total == 0:
            break