import utils
import random
from ga.Chromosome import Chromosome


class Population:
    def __init__(self, count: int):
        self.__population = self.__generate(count)

    def __getitem__(self, item):
        return self.__population[item]

    def set(self, new_population):
        self.__population = new_population

    def select_best(self):
        sorted_population = self.__sort()
        if len(sorted_population) > 1:
            return sorted_population[0:len(sorted_population)-1]
        else:
            return sorted_population

    def crossover(self):
        current_population = self.__population
        new_population = []

        for i in range(len(current_population) - 1):
            for j in range(len(current_population)):
                if j <= i: continue

                new_chromosomes = [
                    current_population[i].selection(current_population[j]),
                    current_population[j].selection(current_population[i])
                ]
                new_population.extend(new_chromosomes)

        new_population = self.__unique_chromosomes(new_population)
        self.set(new_population)

    def mutation(self):
        mutate_index = random.randint(0, len(self.__population) - 1)
        mutated_chromosome = self.__population[mutate_index].mutate()
        print('Мутация: ' + self.__population[mutate_index].value + ' -> ' + mutated_chromosome.value)
        self.__population[mutate_index] = mutated_chromosome

    def print_out(self):
        for x in self.__population:
            print(x.value + ', f = ' + str(x.f()))

    def size(self):
        return len(self.__population)

    def min(self):
        return min(self.__sort(), key=lambda x: x.f())

    def filter(self):
        return list(filter(lambda x: x.f(), self.__population))

    def __sort(self):
        filtered_population = filter(lambda x: x.f(), self.__population)
        return list(sorted(filtered_population, key=lambda x: x.f()))

    @staticmethod
    def __generate(count: int):
        size = len(utils.cities)
        max_value = len(utils.points) - 1
        return [Chromosome(utils.random_chromosome_value(size, max_value)) for i in range(count)]

    @staticmethod
    def __unique_chromosomes(population):
        unique_values = []

        for i in range(len(population)):
            if len(unique_values) == 0:
                unique_values.append(population[i])
                continue

            is_unique = True

            for j in range(len(unique_values)):
                if population[i].value == unique_values[j].value:
                    is_unique = False
                    break
            if is_unique:
                unique_values.append(population[i])

        return unique_values
