def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'O terreno com comprimeiro {comprimento} e largura {largura} possui uma area de {resultado} quadrados.')

largura = float(input('Qual é a largura? '))
comprimento = float(input('Qual o comprimento? '))

area(largura, comprimento)