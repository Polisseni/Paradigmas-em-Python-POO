def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um valor inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um valor inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados INTERROMPIDA pelo usuário!\033[m')
            return 0
        else:
            return n



#Programa Principal
n1 = leiaInt('Digite um valor INTEIRO: ')
n2 = leiaFloat('Digite um valor REAL: ')
print(f'O número inteiro digitado foi {n1} e o número real digitado foi {n2}.')
