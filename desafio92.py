from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['ano_nasc'] = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - cadastro['ano_nasc']
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['ano_contrato'] = int(input('Ano de contratação: '))
    cadastro['sal'] = float(input('Salário: '))
    #cadastro['aposentadoria'] = 35 + (cadastro['ano_contrato'] - cadastro['ano_nasc'])
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['ano_contrato'] + 35) - datetime.now().year)
print('-='*20)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')