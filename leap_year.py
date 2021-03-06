while True:
    try:
        user_input = int(input('Input a year: '))

        if ((2020 - user_input) % 4 == 0):
            print('This is a leap year')
        else:
            print('this is not a leap year')

    except ValueError:
        print('This is not a number')