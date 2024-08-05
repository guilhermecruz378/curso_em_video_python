print('Olá vamos simular seu emprestimo bancario...')
valor_casa = input('Primeiro nos diga o valor da casa: ')
salario = input('Qual seu salario? ')
parcela = input('Quantas parcelas você pretende pagar esse valor? ')

parcela_int = int(parcela)
salario_float = float(salario)
excedencia = salario_float * 0.30 + salario_float
valor_casa_float = float(valor_casa)

parcela_da_casa = valor_casa_float / parcela_int

print(f'O valor parcelado da casa fica {parcela_da_casa:.2f}')
print(f'A sua renda mensal é de {salario_float:.2f} e a parcela da casa é {parcela_da_casa:.2f}')


if parcela_da_casa > excedencia:
    print('Não é possivel o financiamento...')
else:
    print('Vamos concluir o financiamento? ')

#print(excedencia)
