import desafio109mod 

p = float(input('Digite o preço: R$'))
print(f'A metade de {desafio109mod.moeda(p)} é {(desafio109mod.metade(p, True))}')
print(f'O dobro de {desafio109mod.moeda(p)} é {desafio109mod.dobro(p, True)}')
print(f'Aumentando 10% de {desafio109mod.moeda(p)} temos {desafio109mod.aumentar(p, 10, True)}')
print(f'Diminuindo 20% de {desafio109mod.moeda(p)} temos {desafio109mod.diminuir(p, 20, True)}')