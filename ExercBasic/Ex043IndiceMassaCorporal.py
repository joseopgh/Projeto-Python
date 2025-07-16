peso = float(input('Qual é seu peso? (Kg) '))
metro = float(input('Qual é sua altura? (m) '))
imc = peso / (metro ** 2)
print('O IMC dessa pessoa é de {:.2f}'  .format(imc))
if imc < 18.5:
    print ('Você esta a baixo do peso!')
elif imc < 25:
    print ('Você está no seu peso ideal PARABENS!')
elif imc < 30:
    print ('Você está Acima do peso!')
elif imc < 40:
    print ('Você Esta com OBESIDADE!')
else:
    print('Você esra com OBESIDADE MORBIDA \033[0;31mCUIDADO!\033[m')