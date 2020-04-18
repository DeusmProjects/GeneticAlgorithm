import utils


class Chromosome:
    def __init__(self, value: str):
        self.genes = self.__get_genes(value)
        self.value = value

    def __getitem__(self, item):
        return self.genes[item]

    def size(self):
        return len(self.genes)

    def f(self):
        f_value = 0

        for i in range(self.size()):
            gene = self[i]
            if utils.cities[i] <= utils.points[gene]:
                f_value += utils.A[gene][i] + utils.points[gene] - utils.cities[i]
            else:
                return False
        return f_value

    def selection(self, chromosome):
        slice_index = (self.size() // 2) + (self.size() % 2)
        new_value = self.value[0:slice_index] + chromosome.value[slice_index:chromosome.size()]
        return Chromosome(new_value)

    def mutate(self):
        mutate_value = self.value[::-1]
        return Chromosome(mutate_value)

    @staticmethod
    def __get_genes(value: str):
        return list(map(int, value))
