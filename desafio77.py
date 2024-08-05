#tirando vogais das palavras
palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
           'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
           'MERCADO', 'PROGRAMADOR', 'FUTURO' )
for indice in palavra:
    print(f'Na palvra {indice} temos: ')
    for vogal in indice:
        if vogal.lower() in 'aeiou':
            print(f'{vogal}')