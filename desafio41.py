from datetime import date
data_atual = date.today().year

nasc = input('Que ano você nasceu? ')
nasc_int = int(nasc)
faixa_etaria = data_atual - nasc_int

if faixa_etaria <= 9:
    print('Mirin')
elif faixa_etaria >= 10 and faixa_etaria <= 14:
    print('INFANTIL')
elif faixa_etaria >= 15 and faixa_etaria <= 19:
    print('JÚNIOR')
elif faixa_etaria >= 20 and faixa_etaria <= 25:
    print('SÊNIOR')
elif faixa_etaria >= 26:
    print('MASTER')
#else:
#    print('?')