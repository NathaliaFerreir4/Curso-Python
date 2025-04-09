peso = float(input('Digite o seu peso em kg e ultilize o . no lugar da virgula:'))
altura  =float(input('Digite a sua altura ultiizando o . :'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você esta abaixo do seu peso ideal!')
elif imc >= 18.5 and imc <= 25:
    print('Você esta no seu peso ideal!')
elif imc > 25 and imc <= 30:
    print('Você esta sobrepeso!')
elif imc > 30 and imc <= 40:
    print('Você esta obeso!')
else:
    print('Você esta com obesidade morbida!')