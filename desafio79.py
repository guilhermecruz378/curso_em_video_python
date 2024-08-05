#------- VALORES ÚNICOS EM UMA LISTA-------
valores = 0
m_lista = list()
while True: # usei um laço de repetição infinita para o usuario ter controle do limite de repetições
    valores = int(input('Digite um valor: ')) # valor a coletar
    if valores not in m_lista: # se o valor digitado não estiver na lista então minha lista ira receber o valor
        m_lista.append(valores)
        print('VALOR ADICONADO COM SUCESSO...')
    else: # se o valor ja estiver na lista entao na ira adicionar
        print('VALOR DUPLICADO!! NÃO VOU ADICIONAR...')
    continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar in 'Nn':
        break
print('FIM DO PROGRAMA')
print(f'Colhendo seus dados temos a lista com os valores: {sorted(m_lista)}')
