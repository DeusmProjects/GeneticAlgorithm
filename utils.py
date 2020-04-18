import random

cities = [1, 1, 5, 1, 4]
points = [4, 12, 5]

A = [
    [1, 4, 10, 2, 7],
    [2, 2, 1, 9, 5],
    [11, 1, 6, 5, 4]
]


def random_chromosome_value(size, max_digit):
    chromosome_value = ''
    for i in range(size):
        chromosome_value += str(random.randint(0, max_digit))
    return chromosome_value
