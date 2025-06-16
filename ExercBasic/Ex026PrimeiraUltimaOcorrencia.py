frase = str(input('Digite uma Frase: ')).strip()
texto = frase.lower()
print('A letra A aparece {} vezes na frase.' .format(texto.count('a')))
print('A primeira letra A aparece na posição {} '.format(texto.find('a')+1))
print('A ultima letra A aparece na posição {} ' .format(texto.rfind('a')+1))


