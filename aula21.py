# ---------------------------------INTERACTIVE HELP ------------------
# --> help() -> Ele me dá(retorna) as informaçoes ou manuais de casa função
# ex help() print
#help(print)
# posso tambem imprimir todas as informçoes com o - doc -
'''print(input.__doc__)
==
help(input)'''

# --> docstrings
'''São manuais criados para auxiliar na função criada.
Ela é formada na linha de baixo da declaração do comando -def- 
.Para digitar o manual usasse aspas dupla(")

def contador(i, f, p):
    """
    -> Faz uma contagem que mostra na tela
    :param i: início da contagem 
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c{}', end=' ')
        c += p
    print('FIM')

'''

#-------------------------- PARÂMETROS OPCIONAIS ------
'''
São para caso de declarações feitas faltando um valor no parametro
def somar(a,b,c)

somar(1,2,3) Assim não daria problema nenhum na minha função pois todos os valores entrariam no parametro
somar(1,3) Nesse caso darua problema pois está faltando um valor para o parametro 
para fazer funcionar nesse caso fariamos da seguinte forma

def somar(a,b,c=0) Mesmo se eu não digitasse um valor para o parâmetro não daria erro, pois, o 'c' já vale 0
def somar(a=0,b=0,c=0) poderia ser digitado dessa forma sem problema nenhum

def somador(a=0, b=0, c=0):
    """
    -> faz somar.
    :param a: Primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


somador(1,2)'''

# ------------------------------------------- ESCOPO DE VÁRIAVEL ---- 
'''
Temos uma variavel global : a qual ira funcionar em todo o meu programa ou area em que está a minha def e o meu progrma principal.
>>>> 
def teste()
    print(f'Na função teste, o n vale {n} ')


n = 2 
print(f'No programa principal o n vale {n}') <<<<<
nessa area acima o n tera o mesmo valor em ambos os locais pq está sendo declarado fora do def 
por isso ele é uma: -> ...variavel global... ESCOPO GLOBAL
-----------------------
def teste()
    x = 8
    print(f'Na função teste, o n vale {n} ')
    print(f'Na função teste, o x vale {x}')


n = 2 
print(f'No programa principal, o n vale {n}') 
print(f'No programa principal, o x vale {x}')
Nesse caso ocorreria um erro pq o valor de (x) ele só está dentro da função ele só pode ser executado dentro da função
por isso ele é chamado de: ...váriavel local... ESCOPO LOCAL
-----------------------
def teste(b):
    global a -> se eu declarar essa função o 'a' de fora passa a valer o mesmo que o 'a' de dentro e eles passam a ser uma variavel global / escopo global.
    a = 8 -> dentro do escopo local ele vai alterar o valor mas sem alterar o programa principal
    b += 4 -> ele vai somar com a variavel do escopo local 
    c = 2 -> NO escopo local ele ira valer 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'a fora vale {a}')
'''
# --------------------------------- RETORNO DE VALORES ----------------------------- 
# -> return -> é muito útil quando eu quero ter personalização dos resultados 
'''
def somador(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,4,6)
r2 = somar(9,5)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
'''
'''def fatorial(num = 1):
    f = 1
    for cont in range(num, 1, -1):
        f *= cont
    return f

"""n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')"""
f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3} ')'''

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')