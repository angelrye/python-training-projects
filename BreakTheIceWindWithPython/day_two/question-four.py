import sys


def solution_one(args):
    numbers = sys.argv[1]

    list_numbers = numbers.split(',')
    tuple_numbers = tuple(list_numbers)

    print('---------- Solution #1-----------')
    print(list_numbers)
    print(tuple_numbers)
    print('---------------------------------')


def solution_two():
    lst = (input('Enter a number: ')).replace(' ', '')

    lst_nbrs = lst.split(',')

    print(lst_nbrs)
    print(tuple(lst_nbrs))

def main():
    solution_one(sys.argv[1])
    solution_two()


if __name__ == '__main__':
    main()
