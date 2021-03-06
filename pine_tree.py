
try:
    user_input = int(input('Please, input a positive number: '))
    if user_input <= 0:
        print('Your number is not positive')
    else:
        counter = 0
        while counter <= user_input:
            print(('*' * counter) * 2)
            counter += 1

except ValueError:
    print('Incorrect input')


