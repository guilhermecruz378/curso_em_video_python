quant_idade_maior = quantidade_masc = quantidade_female = 0
sexo = continuar = ' '
while True:
    print('CADASTRE UMA PESSOA')
    print('-='*20)
    idade = int(input('Qual sua idade: '))
    while sexo not in 'MF':
        sexo = input('Qual seu sexo: [M/F]').strip().upper()[0]
    print('-='*20)
    if idade >= 18:
        quant_idade_maior += 1
    if sexo == 'M':
        quantidade_masc += 1
    if sexo == 'F' and idade < 20:
        quantidade_female += 1
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos cadastrados é: {quant_idade_maior} ')
print(f'Ao todo temos {quantidade_masc} homens cadastrados...')
print(f'E temos {quantidade_female} mulheres com menos de 18 anos.')