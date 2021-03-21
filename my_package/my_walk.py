import os


def my_walk(path):
    if not os.path.isdir(path):
        return
    return os.listdir(my_walk(path))


if __name__ == '__main__':
    path = input('Input file name: ')
    print(my_walk(path))
