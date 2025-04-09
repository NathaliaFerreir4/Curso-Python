from pacote.cadastro import *
from time import sleep
from pacote.arq import *

arquivo = 'C:/Users/Natália/OneDrive/Área de Trabalho/Python curso emvideo/Erros & Exceções/cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)
    
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resp == 1:
        #Opção de listar o conteudo de um arquivo!
        lerArquivo(arquivo)
        
    elif resp == 2:
        #Opção cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrar(arquivo, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Ate logo!')
        break
    else:
        print('Digite uma opção válida!')
    sleep(2)