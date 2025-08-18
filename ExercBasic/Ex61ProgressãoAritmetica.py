print('Gerador de PA')
print('=-='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = termo + (10 - 1) * razao
c = 0
while decimo <= decimo + razao:
    print('{}'.format(decimo), end=' -> ')
print('FIM')