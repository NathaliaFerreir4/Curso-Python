import requests

def verificação(url):
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            print(f'Isso aí! Você conseguiu acessar {url}')
        else:
            print(f'O site respondeu com o status: {res.status_code}')

    except requests.ConnectionError:
        print('Sem internet ou o domínio esta errado!')
    except Exception as erro:
        print(f'O site nao esta disponivel no momento.')
    

verificação('https://www.pudim.com.br/')
