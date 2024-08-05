def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    
 
#Programa Principal
n = str(input('Nome do jogador: '))
g = input('Número de gols: ')
if g.isnumeric():#Estou verificando se valor na variavel é um número se for...
    g = int(g)# se for número a variavel(g) ira receber ela mesmo como um número int
else:
    g = 0 #Se não ela continua valendo zero
if n.strip() == '':# se na minha string conter apenas um nada então...
    jogador(gols=g)
else:
    jogador(n, g)