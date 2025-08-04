media = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for pessoa in range (1,5):
    print('----- {}ª \033[1;36mPESSOA\033[m -----'.format(pessoa))
    nome = str(input('Nome: ')).strip()  #strip para tirar os espaços
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()

    media = media + idade  #pode usar tbm o "+=" Ex media += idade
    if pessoa == 1 and sexo in 'Mm':            #o nome do homem mas velho
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:     #Mostrando quantos mulheres tem com menos de 20 anos
        totmulher20 += 1


mediaidade = media / 4
print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print('O homem mas velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))     #resultado final
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))