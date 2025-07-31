from datetime import date
idade = date.today().year
totmaior = 0
totmenos = 0
for c in range(0,7):
    data = int(input('Em que ano a {}ª pessoa nasceu? '.format(c+1)))
    ano = idade - data
    if ano >= 21:
        totmaior += 1
    else:
        totmenos += 1
print('''Ao todo tivemos {} pessoal maior de idade
E também tivemos {} pessoa menos de idade'''.format(totmaior, totmenos))