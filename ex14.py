temperatura = int(input('Qual é a temperatura, agora?'))
conversao = (9 * temperatura / 5) + 32

print('A temperatura \033[1;36m{}°C\033[m, corresponde a \033[1;35m{}°F\033[m'.format(temperatura,conversao))