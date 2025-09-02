print('GERADOR DE PA')
print('-='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
cont2 = 1
while cont2 <= mtermo:
    while cont <= 10:
        print('{}'.format(termo), end=' -> ')
        termo = termo + razao
        cont = cont + 1
    print('FIM')
mtermo = int(input('Quantos termos você quer mostrar a mais? '))