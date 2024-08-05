#68 /(1,67*2)
nome = input('Qual seu nome? ')
peso = input('Qual seu peso? (Kg) ')
altura = input('Qual a sua altura? (M)')

peso_float = float(peso)
altura_float = float(altura)
imc = peso_float / (altura_float ** 2)
print(f'Seu imc é {imc:.2f}')

if imc <= 18.5:
   print(f'{nome} Você está Abaixo do peso')
elif imc >= 18.6 and imc <= 25: 
    print(f'{nome} você está no Peso ideal')
elif imc >= 25.1 and imc <= 30:
    print(f'{nome} você está Sobre peso')
elif imc >= 30.1 and imc <= 40:
    print(f'{nome} você está com Obesidade')
else:
    print(f'{nome} você está com Obesidade Mórbida')