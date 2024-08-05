#---------- AULA DE DICIONARIOS ------------
'''
OS DICIONÁRIOS SÃO RESPRESENTADOS POR COLCHETES -> {}
    dados = dict()
    dados = {}
    dados = {'nome':'Pedro', 'idade':25}
            {dados}
            {Pedro,  25}
             nome    idade
    print(dados['nome']) == 'Pedro'
    print(dados['idade']) == 25

PARA ADICIONAR ALGO: 
dados['sexo'] = 'M' -> [pedro, 25, M]

PARA REMOVER ELEMENTOS:
del dados('idade') -> [Pedro, m]

filme = {'titulo':'Star Wars',
'ano':1977, 
'diretor':'George Lucas' 
}
print(filme.values()) -> ira me retornar todos os valores da minha variavel/dicionário == Star Wars, 1977, George Lucas

print(filme.keys()) -> vai me mostrar todas as chaves == titulo, ano, diretor

print(fime.items()) -> vai me retornar tanto os valores como as chaves

NAS ESTRUTURAS DE LAÇOS:
for k, v in filmes.items():
    print(f'O{k} é {v}') == 0 -> O titulo é Star Wars 1 -> o ano é 1977 2 -> o diretor é George Lucas

EU POSSO CRIAR UMA LISTA COM MEU DICIONÁRIO DENTRO:
locador = [{'titulo':'Star Wars','ano':1977, 'diretor':'George Lucas' }, 
{'titulo':'Avenger', 'ano':2012 ,'diretor':'joss whedon'},
{'titulo':'Matrix', 'ano':1999 ,'diretor':'wachowski'} ]

print(locadora[0][ano]) -> 1997
print(locadora[2][titulo]) -> matrix
'''
"""pessoas = {'nome':'guilherme', 'sexo':'M', 'idade':23}
#print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
pessoas["nome"] = 'Douglas'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')"""

'''brasil = []
estado1 = {'uf':'Rio de janeiro', 'sigla':'Rj'}
estado2 = {'uf':'São paulo', 'sigla':'Sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''


estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
"""for e in brasil:
    for k, i in e.items():
        print(f'O campo {k} tem valor {c}')"""
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print('\n')