def divisor_list(*args):
    return result


if __name__ == '__main__':
    try:
        user_input = int(input('Input a number: '))
        nums = list(range(1, user_input + 1))
        divs = filter(lambda x: user_input % x == 0, nums)
        result = list(divs)
        print(result)
    except ValueError:
        print('Incorrect input')