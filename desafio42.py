from math import hypot

primeiro_seg = input('Digite o primeiro segmento: ')
segundo_seg = input('Digite o segundo segmento: ')
terceiro_seg = input('Digite o terceiro segmento: ')

primeiro_seg_float = float(primeiro_seg)
segundo_seg_float = float(segundo_seg)
terceiro_seg_float = float(terceiro_seg)
triangulo = hypot(primeiro_seg_float, segundo_seg_float, terceiro_seg_float)

if primeiro_seg_float < segundo_seg_float + terceiro_seg_float and segundo_seg_float < primeiro_seg_float + terceiro_seg_float and terceiro_seg_float < primeiro_seg_float + segundo_seg_float:
    if primeiro_seg_float == segundo_seg_float == terceiro_seg_float:
        print('Pode-se formar um triângulo EQUILATERO')
        print(f'Resultado do triângulo {triangulo:.2f}')
    elif primeiro_seg_float == terceiro_seg_float or segundo_seg_float == terceiro_seg_float:
        print('pode-se formar um triângulo ISÓSCELES')
        print(f'Resultado do triângulo {triangulo:.2f}')
    elif primeiro_seg_float != segundo_seg_float != terceiro_seg_float:
        print('pode-se formar um triângulo ESCALENO')
        print(f'Resultado do triângulo {triangulo:.2f}')
else:
    print('Não pode ser formado um triângulo')