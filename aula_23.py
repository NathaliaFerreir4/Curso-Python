try:
    a =  int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('Não é possivel divir por 0')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado.')