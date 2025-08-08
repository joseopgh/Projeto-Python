sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]         #upper()[0] So pegou a primeiro letra
while sexo not in 'MnFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

