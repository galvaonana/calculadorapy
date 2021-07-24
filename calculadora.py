def calculate():
    operation = input('''
Escolha o simbolo de acordo com a operação desejada:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    numero_1 = int(input('Coloque aqui o primeiro numero: '))
    numero_2 = int(input('Coloque aqui o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operation == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operation == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('Você escolheu um operador não válido, tente novamente')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Você quer calcular de novo?
Escreva Y para SIM or N for NAO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Ate mais yag!')
    else:
        again()

calculate()