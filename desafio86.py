# ------- MATRIZ ------------
matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
for l in range(0,3): #um laço para colher valores # esse for virou uma contagem para o proximo laço
    for c in range(0,3): #esse laço é o colherdor enquanto o anterior está contando o laço
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #
for l in range(0,3): #igualmente o anterior ele está contando
    for c in range(0,3):# nesse laço ao inves de colher os valores na contagem ele vai motrar na contagem
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print('\n')