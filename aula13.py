# laços de repetiçoes iteraçôes 
'''
laço c no intervalo(0,10): -> c == uma variavel de controle
    passo 
pega -> pega estáfora do bloco de identação então está fora do laço
---------------------------------------------------------------
forma de escrever em python é;
for c in range(0, 10):
    passo
pega
---------------------------------------------------------
for c in range(0,10):
    se moeda:
        pega
    passo
    pula
passo
pega

'''
'''for contador in range(0,11):
    print(contador)
    print('oi')
print('Fim')'''

'''for contador in range(11, 0, -1):
    print(contador)
print('Fim')'''

'''for c in range(0, 3):
    n = int(input('Digite um número:'))
print('Fim')'''

'''i = int(input('Começo: '))
f = int(input('Digite o fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, 1):
    print(c)
print('Fim')'''

soma = 0

for c in range(0, 10):
    soma = soma + c
print(soma)