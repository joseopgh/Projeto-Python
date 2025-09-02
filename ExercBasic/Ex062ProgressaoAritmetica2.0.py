print('GERADOR DE PA')
print('-='*20)                                                     #cabeçario do codico
termo = int(input('Primeiro termo: '))                             #introdução da variaveis
razao = int(input('Razão da PA: '))
cont = 1                                                           #contador do while
total = 0                                                          #contador do while termos
mtermo = 10
while mtermo != 0:                                                 #Laço para quantos mas voc queres
    total = total + mtermo                                         #contador do laço
    while cont <= total:                                           #primeiro laço
        print('{}'.format(termo), end=' -> ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mtermo = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termo mostrados.'.format(total))