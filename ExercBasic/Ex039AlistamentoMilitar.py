from datetime import date
ano = date.today().year
print('Se você for HOMEM digite [ 1 ]')
print('Se você for MULHER digite [ 2 ]')
sexo = int(input('Qual seu sexo? '))
if sexo == 1:
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
elif sexo == 2:
    print('Você não precisa se alista no serviço militar.')
else:
    print('Numero Digitado incorreto.')
