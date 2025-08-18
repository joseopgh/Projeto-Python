print('Gerador de PA')
print('=-='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = termo
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo = termo + razao
    cont = cont + 1
print('FIM')
