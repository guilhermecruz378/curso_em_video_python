from datetime import date
ano = input('Qual ano você nasceu? ')
data_atual = date.today().year

ano_int = int(ano)
idade = data_atual - ano_int

if idade > 18:
    print('Você perdeu o prazo para seu alistamento.')
    saldo = idade - 18
    print(f'Você deveria ter se alistado a {saldo} anos atrás')
    print(f'Seu alistamento foi em {2024 - saldo}')
elif idade < 18:
    print('Ainda não chegou o seu ano de alistamento...')
    print(f'Faltam {18 - idade} anos para seu alistamento')
elif idade == 18:
    print('Você precisa se alistar imediatamente!!! ')
else:
    print('?')

