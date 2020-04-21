import random

cities = [1, 2, 5, 6, 4]  # города, которые должны получить продукты
points = [3, 5, 7]  # пункты, которые производят продукты

# матрица стоимости перевозок из каждого пункта в каждый город
A = [
    [1, 4, 10, 2, 7],  # для пункта 0
    [2, 2, 1, 9, 5],  # для пункта 1
    [11, 1, 6, 5, 4]  # для пункта 2
]


def random_chromosome_value(size, max_digit):
    chromosome_value = ''
    for i in range(size):
        chromosome_value += str(random.randint(0, max_digit))
    return chromosome_value
