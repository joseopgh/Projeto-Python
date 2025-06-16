nome = str(input('Qual é seu nome completo? ')).strip()
name = nome.lower()
print('Seu nome tem Silva? {} '.format(name.find('silva')>0))
