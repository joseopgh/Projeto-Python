from datetime import date
ano = date.today().year
nasceu = int(input('Ano de nascimento: '))
idade = ano - nasceu
print('Quem nasceu em {} tem {} ano em {}.'.format(nasceu, idade, ano))
if idade == 18:
    print('Você tem que se alistar \033[0;31mIMEDIATAMENTE!\033[m')
elif idade > 18:
    print('Você ja deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(nasceu + 18))
else:
    print('Ainda falta {} anos para o alistamento' .format(18 - idade))
    print('Seu alistamento será em {}.'.format(nasceu + 18))