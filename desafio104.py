def LeiaInt(msg):
    ok = False #indiquei um valor falso
    valor = 0 #o valor
    while True: #enquanto for verdadeiro
        n = str(input(msg)) # o n recebe um input de msg
        if n.isnumeric(): #se n for numerico ele faz
            valor = int(n) # valor receber o n formatado em int
            ok = True # ok recebe o verdadeiro
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor

n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')