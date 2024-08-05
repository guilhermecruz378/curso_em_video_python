#------LISTAS DENTRO DE LISTA------
'''
dados = [pedro,25]
           0    1
pessoa = list()
pessoa.apend(lista[:]) -> vai me dar uma copia de dados

pessoa = [[pedro,5],[maria,19],[joao,32]]
             0          1          2 
print(pessoa[0][0]) -> 'pedro'
print(pessoa[1][1]) -> '19'
print(pessoa[2][0]) -> 'joao' 
print(pessoa[1]) -> 'maria,19'
'''

'''galera = [['joao',19], ['maikao',25], ['guilherme', 23], ['evelin',22]]
#print(galera[2][0])
for pessoa in galera:
#    print(pessoa)
#    print(pessoa[0])
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''
lista = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    lista.append(dado[:])
    dado.clear()
#print(lista)
for c in lista:
    if c[1] >= 25:
        print(f'{c[0]} tem idade maior que 25')
        totmaior += 1
    else:
        print(f'{c[0]} é menor de idade')
        totmenor += 1

print(f'temos {totmaior} maiores de idade e {totmenor} de menores de idade')