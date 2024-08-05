def LeiaInt(x):
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUSUARIO descidio não digitar esse númer.\033[m')
            return 0
        else:
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO REAL VÁLIDO!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUSUARIO descidio não digitar esse númer.\033[m')
            return 0
        else:
            return n
            

'''n = input('Digite um número inteiro: ')
z = input('Digite um número Real: ')
print(LeiaInt(n))
print(LeiaFloat(z))'''
n = LeiaInt('Digite um numero inteiro: ')
z = LeiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado é {n} e o real foi {z}')
#### PROGRAMA IGUAL AO DO PROFESSOR MAS NÃO EXECUTA CORRETAMENTE, ACHAR A SOLUÇÃO!