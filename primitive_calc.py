while True:
    try:
        number_1 = int(input('Input number 1: '))
        oper_sign = input('Input operation: ')
        number_2 = int(input('Input number 2: '))
        if oper_sign == '+':
            print(number_1 + number_2)
        elif oper_sign == '-':
            print(number_1 - number_2)
        elif oper_sign == '*':
            print(number_1 * number_2)
        elif oper_sign == '/':
            print(number_1 / number_2)

        else:
            print('Operation sign is incorrect')




    except ValueError:
        print('Incorrect input')

    except ZeroDivisionError:
        print('Zero can not be a divisor')

