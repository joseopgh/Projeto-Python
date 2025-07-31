from datetime import date
idade = date.today().year
for c in range(0,7):
    data = int(input('Em que ano a {}ª pessoa nasceu? '.format(c+1)))
    ano = idade - data
print('''Ao todo tivemos {} pessoas maiores de idade
E Também tivemos {} pessoa menores de idade'''.format)
