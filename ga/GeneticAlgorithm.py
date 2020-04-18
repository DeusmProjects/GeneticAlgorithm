from ga.Population import Population


class GeneticAlgorithm:
    def __init__(self, population_count, steps_count):
        population = Population(population_count)
        print('Первое поколение: ')
        population.print_out()
        print('_____________')

        i = 0
        while (i < steps_count) & (population.size() > 1):
            new_population = population.select_best()
            if len(new_population) == 1:
                break

            population.set(new_population)
            print('Лучшие особи: ')
            population.print_out()

            population.crossover()
            population.mutation()

            print('Поколение', i + 2)
            population.print_out()

            i += 1
            print('_____________')

        print('Последнее поколение')
        population.print_out()
        optimal = population.min()
        print('Оптимальный маршрут: ', optimal.value, optimal.f())
