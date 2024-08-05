primeira_nota = input('Digite a primeira nota: ')
segunda_nota = input('Digite a segunda nota: ')

primeira_nota_float = float(primeira_nota)
segunda_nota_float = float(segunda_nota)

media = primeira_nota_float + segunda_nota_float / 2
print(f'Sua média é {media}')

if media >= 7.0:
    print(f'Sua primeira nota foi {primeira_nota_float} e sua  segunda nota foi {segunda_nota_float}')
    print('Aluno APROVADO!!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua primeira nota foi {primeira_nota_float} e sua  segunda nota foi {segunda_nota_float}')
    print('Aluno em RECUPERAÇÃO!')
else:
    print(f'Sua primeira nota foi {primeira_nota_float} e sua  segunda nota foi {segunda_nota_float}')
    print('Aluno REPROVADO')
