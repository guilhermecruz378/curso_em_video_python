# -------- Teste se o site pudim está acessivel -----------
import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Não consegui acessar o site.')
else:
    print('Consegui acessar o site')