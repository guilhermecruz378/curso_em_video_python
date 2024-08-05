'''sexo = ''
m = 'M'
f = 'F'
while sexo == '':
    escolha = input('Informe seu sexo: [M/F] ').strip().upper()
    if escolha == m or f:
        if escolha == m:
            sexo = m
            print('Você é homem')
            break
        if escolha == f:
            sexo = f
            print('Você é mulher')
        else:
            print('dados invalidos por favor', end=' ')
print('Dados coletados')'''

sexo = input('Informe seu sexo: [M/F]').strip().upper()[0]
while sexo not in 'FM':
    sexo = input('opção inválida. por favor, informe seu sexo: ').strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso')

