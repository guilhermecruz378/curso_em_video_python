#----------------TUPLAS------------------
'''
quando uma variavel é declarada ela vira um espaço na memoria
,armazena um espaço na memoria. 
uma variavel simples só pode obter 1 valor(dado) nela
uma variavel composta pode caber mais que 1(varios valores) são 3 tipos
eles são:
1.Tuplas
2.listas
3.dicionarios

Uma tupla é declarada como variavel e usamos os parentese () e separamos cada variavel po virgula ,
tupla = ('lanche', 'suco', 'Batata')


print(lanche[2])
print(lanche[0:2]) = 0,1 / Fatiamento
len(lanche) = 4 == quantos elementos tem a variavel lanche
uso das estruturas de repetiçoes
for 'c' in lanche :

-------AS TUPLAS SÃO IMUTAVEIS PECULIARIDADE DAS TUPLAS ------
AS TUPLAS SÃO USADAS EM UMA VARIAVEL COMUM E DEVE SER COLOCADAS EM ()
AS TUPLAS SÃO USADAS COM '()' - PARENTESES
'''

#lanche = ('Hamburguer', 'suco', 'pizza', 'pudin')
#print(sorted(lanche))
#print(len(lanche))
#print(lanche[0:4:3])
'''for comida in lanche : # para cada comida in lanche
    print(f'Eu vou comer {comida}')
print('Comi demais')'''

'''for c in range(len(lanche)):
    #print(lanche[c])
    print(f'Eu vou comer {lanche[c]} na posição {c}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''


"""a = (2, 5, 4)
b = (7, 8, 5, 6)
c = a + b
print(c.index(6))"""

pessoa = ('guilherme', 23, 78.00 , 1.68)
#del(pessoa) #não se pode apagar um item de uma tupla só é possivel apagar ela toda
#print(pessoa)

for contador in range(len(pessoa)):
    print(f'O sr {pessoa[contador]} dado {contador} ')

#usasse o len quando eu quero minha string em inteiro caso não usasse sem o len