print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(termo, 11, razao):
    print('{} ->'.format(c), end=' ')
print('ACABOU')