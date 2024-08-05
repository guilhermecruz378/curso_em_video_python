aluno = {}
aluno['Nome'] = input('Qual nome do aluno: ')
aluno['media'] = float(input(f'Qual a média do {aluno["Nome"]}: '))
if aluno["media"] >= 7.0:
    aluno['situação'] = 'APROVADO!!'
elif 5 <= aluno['media'] < 7.0:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = "Reprovado"
print('-='*20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')