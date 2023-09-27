from functools import reduce


def q1_for_list():
    numbers = []
    for num in range(2000, 3201):
        if (num % 7 == 0) and (num % 5 != 0):
            numbers.append(str(num))

    print(','.join(numbers))


def q1_generator_comprehension():
    print(*(i for i in range(2000, 3201) if i %
          7 == 0 and i % 5 != 0), sep=',')


def q2_factorial():
    number = int(input('Enter a number: '))

    print('Recursive function')
    print(fact(number))

    print('\nLambda Expression')
    print(q2_factorial_lambda(number))

    print('\nAccumulator (Reduce) function')
    print(reduce(q2_factorial_reduce_accumulator, range(1, number+1), 1))


def fact(num):
    if (num == 0):
        return 1

    return num * fact(num - 1)


def q2_factorial_lambda(x): return 1 if x <= 1 else x*q2_factorial_lambda(x-1)


def q2_factorial_reduce_accumulator(acc, num):
    return acc*num


def q3_solution_one():
    num = int(input('Enter a number: '))

    num_dict = dict()

    for x in range(1, num+1):
        num_dict[x] = x*x

    print(num_dict)


def q3_solution_dict_comprehension():
    num = int(input("Enter a number: "))
    print({i: i*i for i in range(1, num+1)})
