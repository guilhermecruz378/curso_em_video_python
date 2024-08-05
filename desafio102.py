'''def fatorial(a=0,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param a: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número a.
    """
    print('-'*30)
    if show == False:
        f = 1
        for nuns in range(a, 1, -1):
            f *= nuns
        return f
    else:
        f = 1
        for c in range(a, 1, -1):
            f *= c
            print(f'{c} x', end=' ')
        return f'= {f}'



print(fatorial(4, True))'''

# RESOLUÇÃO DO PROFESSOR 
def fatorial(n, show=False):
    f = 1 
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))

