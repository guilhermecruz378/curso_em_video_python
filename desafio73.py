brasileirao = ('Palmeiras', 'grêmio', 'Atletico-MG', 'Flamengo', 'Botafogo', 
               'Bragantino','Fluminense','Atletico-PR', 'Internacional','Fortaleza',
               'são paulo', 'cuiabá','Corinthians', 'Cruzeiro', 
               'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'America-MG')
print(f'lista de times do brasileirão é: {brasileirao}')
#for c in (brasileirao):
#    print(c)
print('='*15)
print(f'os 5 primerios são {brasileirao[0:6]}')
print('='*15)
print(f'Os 4 ultimos são: {brasileirao[-4:]}')
print('='*15)
print(f'Em ordem alfabetica eles ficam: {sorted(brasileirao)}')
print('='*15)
print(f'Chapecoense esta em : {brasileirao.index('Corinthians')+1}ºlugar')