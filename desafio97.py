"""def mensgaem(msg):
    pos = 0
    while pos < len(msg):
        print('~',end='')
        pos += 1
    print()
    print(f'{msg:^5}')
    pos = 0
    while pos < len(msg):
        print('~',end='')
        pos += 1
    print()"""
    
#Resolução do professor
def mensgaem(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


mensgaem('Capivara bebendo água!')
mensgaem('book2')
mensgaem('Estudando com o Guanabara')