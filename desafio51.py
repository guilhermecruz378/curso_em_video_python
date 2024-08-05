

p = int(input('Primeiro termo: '))
r = int(input('A Razão: '))
d = p + (10 -1) * r # meu primeiro número + (numero desejado - 1) * a minha razão
for pa in range(p, d + r, r):
    print(pa, end='->')
    
print('Acabou')