from datetime import date
nasceu = date.today()
ano = int(input('Ano de Nascimento: '))
idade = nasceu.year - ano
print('O atleta tem {} anos.' .format(idade))
if idade <5:
    print('Desculpa não tem idade suficiente.')
elif idade <= 9:
    print('CATEGORIA: Mirim!')
elif idade <= 14:
    print('CATEGORIA: Infantil!')
elif idade <= 19:
    print('CATEGORIA: Junior!')
elif idade <= 25:
    print('CATEGORIA: Senior!')
elif idade > 25 and idade <= 50:
    print('CATEGORIA: Master!')
elif idade > 50:
    print('APOSENTADO!')
