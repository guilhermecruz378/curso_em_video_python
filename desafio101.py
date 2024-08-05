'''from datetime import date

def voto(data=0):
    """
    -> Retorna se o voto é obrigatório, opcional ou não vota
    :param data: Digite o ano de nascimento
    """
    print('-='*20)
    ano_nascimento = int(input('Em que ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print(f'Você tem {idade} anos de idade, então...')
    if ano_atual - ano_nascimento <= 17 and ano_atual - ano_nascimento >= 16 :
        print('Seu Voto é opcional.')
    elif ano_atual - ano_nascimento > 17:
        print('Seu Voto é obrigatório')
    else:
        print('Você não pode votar')
    print('-='*20)

#ano_nascimento = int(input('Em que ano você nasceu? '))
voto()
help(voto)'''

#RESOLUÇÃO DO PROFESSOR

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
