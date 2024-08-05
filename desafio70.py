print('LOJA SUPER BARATÃO')
print('-'*20)
total = totmil = contador = pre_menor = 0
barato = ' '
while True:
    produto = input('Escolha um produto: ')
    preço = float(input('Qual o preço do produto: $'))
    total += preço
    contador += 1
    if preço > 1000:
        totmil += 1
    if contador == 1 or preço < pre_menor :
        pre_menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Você quer continuar: [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total de compra foi ${total:.2f} reais')
print(f'Temos {totmil} produto a cima de $1000,00')
print(f'O produto mais barato foi {barato} custou ${pre_menor}')