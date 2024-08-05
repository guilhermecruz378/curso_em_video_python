from time import sleep
"""
lista = []
nome = []
média = 0
while True:
    nome.append(input('Nome: '))
    nome.append(float(input('Nota 1: ')))
    nome.append(float(input('Nota 2: ')))
    média = (nome[1] + nome[2]) / 2
    nome.append(média)
    lista.append(nome[:])
    nome.clear()
    média = 0
    cont = ' '
    while cont not in 'SsNn':
        cont = input('Quer continuar: ').strip()[0]
    if cont == 'N' or cont == 'n':
        break
print('-='*20)
print('Nº'  ,'Nome',f'{'Média': >10}')
print('-'*20)
for c, i in enumerate(lista):
    print(c, f'{i[0]: <10}',f'{lista[c][3]}' )

while True:
    aluno = int(input('Qual aluno Você deseja mostrar a nota? (999 interrompe) '))
    sleep(1)
    if aluno == 999:
        break
    print(f'Notas de {lista[aluno][0]} são [{lista[aluno][1]}, {lista[aluno][2]}] ')
print('PROGRAMA FINALIZADO...')"""

ficha = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    cont = ' '
    while cont not in 'SsNn':
        cont = input('Quer continuar: ').strip()[0]
    if cont == 'N' or cont == 'n':
        break
print('-='*20)
print(f'{'Nº':<5}{'Nome':<10}{'Média'}')
print('-'*20)
for c, i in enumerate(ficha):
    print(f'{c:<5}{i[0]:<10}{i[2]:.2f}')
while True:
    aluno = int(input('Qual aluno Você deseja mostrar a nota? (999 interrompe) '))
    sleep(1)
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno <= len(ficha) - 1:
        print(f'Notas de {ficha[aluno][0]} são [{ficha[aluno][1]}] ')
print('PROGRAMA FINALIZADO...')