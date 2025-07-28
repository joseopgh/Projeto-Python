frase = str(input('Digite uma frase: ')).strip().upper()            #Leu a Frase
palavras = frase.split()                                            #Gera uma lista
junto = ''.join(palavras)                                           #junto a lista para eliminar espaços
inverso =''
for letra in range(len(junto)-1, -1, -1):                           #Fez o Inverso da Lista
    inverso += junto[letra]
print ('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:                                                #TEsto para ver se era ou não Palindromo
    print('Temos um Palindromo!')
else:
    print('A frase digitada não é um Palindromo!')
