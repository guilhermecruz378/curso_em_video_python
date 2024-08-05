lista = []
b = 0
express = input('Digite sua expressão: ')
for bening in express:
    if bening == '(':
        lista.append('(')
    elif bening == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!! ')