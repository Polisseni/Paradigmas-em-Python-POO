try:
    a = int(input('Digite o NUMERADOR: '))
    b = int(input('Digite o DENOMINADOR: '))
    d = a / b
except (ValueError, TypeError):
    print('Tivemos problemas com o TIPO DE DADOS que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por ZERO.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os DADOS.')
else:
    print(f'O resultado é {d:.2f}')
finally:
    print('VOLTE SEMPRE! Muito obrigado!!')
