lista = list()
for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c}: '))) #função para fazer minha lista receber valores + digitados 
print('='*30)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor é {max(lista)} está na posição', end=' ') #função para achar o maior valor na lista
for c, v in enumerate(lista): # usei um laço para obter o tamanho da lista digitado anteriormente
    if v == max(lista): #a estrutura de controle foi usada para obter apenas a localizção do maior valor na lista 
        print(c,'...',end=' ')
print(f'\nO menor valor é {min(lista)} está na posição', end=' ')
for c, v in enumerate(lista):
    if v == min(lista):
        print(c,'...',end=' ')

# ------ SOLUÇÃO DO PROFESSOR ------- 
'''
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
if c == 0:
    maior = menor = 0
    else: 
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
#O restante utilizando o laço -for- foi identico

'''