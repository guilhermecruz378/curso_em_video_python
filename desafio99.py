
'''def contador(* num):
    print('-='*30)
    contador = 0
    print('Análisando os valores passados...')
    for c in num:
        print(c, end=' ')
        if c == 0:
            contador = c
        else:
            if c > contador:
                contador = c
        
    print(f'Foram informados {len(num)} valores ao todos.')
    print(f'O maior valor informado foi {contador}.')
    print('-='*30)


contador(1,2,3)
contador(3, 5, 6, 9, 1)
contador()'''

#Resolução do professro
from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-='*30)
    print('\nAnálisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} Valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior(0)