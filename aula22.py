# ---------- Modulos e Pacotes -------------
# É construir modulos 
# oque é modulos?

# foco dos modulos: 1dividir um programa grnade 2facilitar na legibilidade 3facilitar na manutenção.
'''
Eu preciso criar uma função colacala em uma pasta que esteja em (.py) no fim 
ao criala eu preciso importar a pasta\função para meu programa

from random(modulo) import randint(função)
'''

import aula22mod
num = int(input('Digite um valor'))
fat = aula22mod.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {aula22mod.dobro(num)}')

"""
VANTAGENS DE UTILIZAR OS MÓDULOS:
.Organizção do código
.Facilidade na manutenção
.Ocultação do código detalhado
.Reutilização em outros projetos
"""

# ----------------- PACOTES / BIBLIOTECA ----------------
# PACOTE É UMA PASTA QUE CONTÉM MODULOS
# POSSO SEPARAR POR ASSUNTOS.
# CRIASSE UM PACOTE COM O NOME DAS FNÇOES