#  ----- FUNÇÕES -----
# É uma rotina posso tranformar algo que eu uso sempre em uma função -> def
# def == definição de função
# def é uma funcionalidade criada por alguem na hora
'''def mostralinha():
    print('-'*30)
mostralinha()
print('   Sistema de Alunos   ')
mostralinha()
mostralinha()
print('   Cadastro de funcioários   ')
mostralinha()
mostralinha()
print('   ERRO DO SISTEMA   ')
mostralinha()
'''
"""def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)
mensagem('Ola, Mundo!')"""

'''def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma(b=14, a=2)
soma(a=89, b=7)
soma(45, 5)'''

# empacotamento é colocar varios números e informçoes para dar o parametro infinito (*num)
# def contador(*num): o asteristico é o simbolo de desempacotar 
# ao mostrar na tela ele retornará uma tupla

"""def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')
'''    for valor in núm:
        print(valor)
#    print(núm)'''
    

contador(4,5,4)
contador(8,9,2,2,2)
contador(7,8)"""

valores = []
def dobra(ast):
    pos = 0
    while pos < len(ast):
        ast[pos] *= 2
        pos += 1
valores = [8, 4, 2, 3, 6]
dobra(valores)
print(valores)