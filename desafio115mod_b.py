from desafio115mod_a import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt == leitura de texto / vamos abrir para texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt+ == escreve um arquivo texto e se não existir ele cria
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt') 
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())