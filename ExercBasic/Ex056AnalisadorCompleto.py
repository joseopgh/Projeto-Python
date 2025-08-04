media = 0
for pessoa in range (1,5):
    print('----- {}ª \033[1;36mPESSOA\033[m -----'.format(pessoa))
    name = str(input('Nome: '))
    idade = int(input('Idade: '))
    Sexo = str(input('sexo [M/F]: '))

    media += pessoa
    idmedia = media / 4

print('A média de idade do grupo é de {} anos'.format(idmedia))