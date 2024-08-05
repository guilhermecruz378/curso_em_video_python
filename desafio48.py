# soma de todos os números divisiveis por 3 entre 1 a 500
# n % 3 == 0

soma = 0 # -> Essa variavel para somar os outros valores dentro do range chamamos de acumuladores.
cont = 0 # -> o acumulador de cima estamos usando para somar todos os valores e o de baixo para contar os valores achados!

for contador in range(1, 501, 2):
#    if contador % 2 != 0: # -> poderiamos usar essa formula para chegar ao resultado
        if contador % 3 == 0:
#            soma = soma + contador # cada numero dentro do if é somado com o proximo
             soma += contador
#            cont = cont + 1 # cada numero achado conta mais um numero achado
             cont += 1
print(f'A soma de todos os {cont} valores é igual á {soma}')
