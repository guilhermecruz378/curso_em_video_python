import desafio108moeda 

p = float(input('Digite o preço: R$'))
print(f'A metade de {desafio108moeda.moeda(p)} é {desafio108moeda.moeda(desafio108moeda.metade(p))}')