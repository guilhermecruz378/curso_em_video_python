"""a = float(input('largura (m) '))
b = float(input('comprimento (m) '))
def area(a, b):
    s = 0
    s = a * b
    print(f'A área de um terreno {a}x{b} é igual a {s}')
   
area(a, b)
"""
#resolução do professor
def àrea(larg, comp):
    a = larg * comp
    print(f'A àrea de um terrego {larg} x {comp} tem {a}')


print(' Controle de terreno ')
print('-'*20)
l = float(input(' Largura (m) '))
c = float(input(' Comprimento (m) '))
àrea(l, c)
