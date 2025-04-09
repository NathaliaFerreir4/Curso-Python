from datetime import datetime
anoAtual = datetime.now().year

def voto(nasc):
    idade = anoAtual - nasc
    if idade < 16:
        return(f'Com {idade} anos: NÃO VOTA!')
    elif 16 <= idade >= 18 or idade >= 65 :
        return(f'Com {idade} anos: O seu voto é OPCIONAL!')
    else:
        return(f'Com {idade} anos: OBRIGATÓRIO a votar')


nasc = int(input('Qual é o ano do seu nascimento? '))
print(voto(nasc))