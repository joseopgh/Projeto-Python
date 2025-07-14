nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media < 5:
    print('Sua media foi \033[0;34m{:.2f}\033[m portanto você esta \033[0;31mREPROVADO!\033[m'.format(media))
elif media >= 5 and media < 7:
    print('Sua media foi de \033[0;34m{:.2f}\033[m portanto você esta de \033[0;33mRECUPERAÇÃO!\033[m'.format(media))
else:
    print('Sua media foi de \033[0;34m{:.2f}\033[m portanto você esta \033[0;32mAPROVADO!\033[m'.format(media))