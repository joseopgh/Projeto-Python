print('-='*20)
print('Analisador de Triângulos')
print('=-'*20)
a = float(input('Primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < c + a and c < a + b:            #Forma para forma triangulo
    print('Os segmentos acima PODEM FORMA triangulo!')
else:
    print('Os segmentos a cima Não PODEM FORMA triangulo!')
