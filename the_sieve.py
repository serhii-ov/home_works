try:
    user_input = int(input('Input number: '))
    initial_list = [0] * user_input
    for i in range(user_input):
        initial_list[i] = i

    a = 2
    while a < user_input:
        if initial_list[a] != 0:
            j = a * 2
            while j < user_input:
                initial_list[j] = 0
                j = j + a
        a += 1

    prime_numbers = []
    for i in initial_list:
        if initial_list[i] != 0:
            prime_numbers.append(initial_list[i])

    print(prime_numbers)

except ValueError:
    print('Only numbers, please!')





