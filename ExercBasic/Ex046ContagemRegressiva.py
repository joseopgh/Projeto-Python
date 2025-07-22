import time
inicio = input('Pode começar? ')
if inicio == 'sim':
    for c in range(10,-1,-1):
        print(c)
        time.sleep(1)
    print('BUuuUuUuumMmmmMmmMM')
elif inicio == 'nao':
    print('Aguardando confirmação')
else:
    print('Comando INVALIDO')