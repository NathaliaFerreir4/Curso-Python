from pacote.cadastro import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um erro na criação ddo arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

    
def lerArquivo(nome):
    print(f'Tentando abrir o arquivo: {nome}')
    try:
        with open(nome, 'rt') as a: 
            cabeçalho('Pessoas cadastradas')
            for linha in a:
                dados = linha.strip().split(';')
                nome = dados[0]
                idade = dados[1]
                print(f'{nome:<30} {idade:>3} anos')
    except:
        print(f'Erro ao ler o arquivo')


def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado! :)')
            a.close()