idade_soma = 0
mais_velho = 0
mais_novo = 0
genero_m_qtd = 0
genero_f_qtd = 0
nome_mais_velho = ''

for c in range(1, 5):
    print('-='*3, f'a {c}ª pessoa', '-='*3)
    nome = input('Digite seu nome:').strip()
    idade = int(input('Qual sua idade: '))
    sexo = input('SEXO [M/F]: ').upper().strip()
   
    idade_soma += idade
    if idade == 1:
        mais_velho = idade
    
    if idade > mais_velho:
        mais_velho = idade 
        nome_mais_velho = nome
    if idade < mais_velho:
        mais_novo = idade
    if sexo == 'M':
        genero_m_qtd += 1
    if sexo == 'F':
        genero_f_qtd += 1 

media = idade_soma / 4 

print(f'O mais velho tem {mais_velho} anos e se chama {nome_mais_velho}')
print(f'a media de idade é {media:.0f}')
print(f'Ao todo são {genero_f_qtd} mulheres ')
