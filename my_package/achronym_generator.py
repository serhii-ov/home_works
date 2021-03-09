def achronym_gen(*args):
    return result


if __name__ == '__main__':
    user_input = input(' entre a phrase: ')
    new_list = list(user_input.split())
    counter = 0
    result = ''
    while counter < len(new_list):
        letter_1 = new_list[counter][0].upper()
        result += letter_1
        counter += 1
    print(result)