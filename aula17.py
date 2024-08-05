''' --------  VARIAVEL [LISTAS] ---------
AS LISTAS DIFERENTES DA TUPLA É USADA COM COLCHETES []
AS LISTAS NÃO SÃO IMUTAVEIS ELA PODE SER MUDADA DE ACORDO COM O PROGRAMA
ELA É MUTAVEL

EX: lanche = ['lanche', 'suco', 'Batata']
    lache[2] = 'pizaz'
    print(lache) == lanche, suco, pizza

PARA ADICIONAR ALGO NAS LISTAS:
    lanche.append('cookie') == Esse comando(append) adiciona mais um valor/elemento no final da  sua lista
    lache.insert(0,'cachorro quente') == Esse comando adiciona um valor na localização desejada e joga os outros para frente

PARA ELIMINAR ALGO NAS LISTAS:
    del lanche[2] == Ele vai elinar algo nessa posição/indice
    lanche.pop(2) == Tambem vai eliminar algo nessa posição, normalmente esse comando é usado para elinar algo na ultima posição
    lanche.pop()
    lanche.remove('suco') == Nesse comando você não vai indicar a posição/indice mas sim o valor
    SE EU TENTAR REMOVER UM VALOR INEXISTENTE DO PROGRAMA VOU RECEBER UM ERRO
    MAS EM CONTRA PARTIDA POSSO USAR UM -if- PARA FAZER ESSA JOGADA.
    if 'pizza' in lanche:
        lanche.remove('pizza')

CRIANDO UM RANGE COM AS LISTAS:
    valores = list.range(4,11) == 4,5,6,7,8,9,10
                                [ 0 1 2 3 4 5 6]-> cada valor ira corresponder a esse indice nas listas
    podemos fazer de forma desordenada tambem
    valores = [8,2,5,4,9,3,0]
              [0 1 2 3 4 5 6] -> indice correspondente aos valores
    valores.sort() == ira ordenar os valores -> [0,2,3,4,5,8,9]
    valores.sort(reverse=true) == ira ordenar os valores de forma inversa -> [9,8,5,4,3,2,1,0]

PARA SABER A QUANTIDADE DOS VALORES DAS LISTAS:
    len(valores)

PECULIARIDADE DA LISTA NO PYTHON -ELO DE LIGAÇÃO-
    O python cria uma ligação quando se tenta fazer uma copia de uma lista
    a = list(1,2,3,4)
    b = a 
    b[2] = 8
    print(a) -> 1,2,8,4
    print(b) -> 1,2,8,4
    
    Uma forma de romper essa ligação e criar uma copia é usarmos o fatiamento de strings:
    b = a[:] -> dessa forma se criara uma copia e não uma ligação cria uma copia de -a- para -b-
    a = list(1,2,3,4)
    b = a[:] 
    b[2] = 8
    print(a) -> 1,2,3,4
    print(b) -> 1,2,8,4
'''

"""
num = [4,2,3,5,9]
num[2] = 7 
num.append(11)
num.sort(reverse=True)
num.insert(2,0)
num.pop(2)
if 8 in num:
    print(f'{num.remove(8)}')
else:
    print('valor de exclusão não encontrado')
print(num)
print(len(num))
"""

"""
valores = list()
valores.append(1)
valores.append(8)
valores.append(9)
'''for v in valores: #-> Para obter apenas os valores das minhas listas
    print(f'{v}...',end=' ')'''
for c, v in enumerate(valores):# Se eu quiser além dos valores os indices das chaves eu uso o -for-  dessa forma
    print(f'Na posição {c} encontrei o valor {v}!') # a variavel -c- indica a posição ea variavel -v- indica o valor dentre da lista
print('Cheguei ao final da lista!')

"""

lista = list()
for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))
#lista.sort()
for posição, valor in enumerate(lista):
    print(f'Na posição {posição} eu tenho o valor {valor}')
print('Cheguei ao fim da lista...')