import utils
import sys


class ExhaustiveSearch:
    def __init__(self):
        self.__cities_count = len(utils.cities)
        self.__points_count = len(utils.points)

        item = [0] * self.__cities_count
        optimal_f = self.__f(item)
        optimal_item = item.copy()

        if not optimal_f:
            optimal_f = sys.maxsize

        for i in range(self.__points_count ** self.__cities_count - 1):
            next_item, f = self.__generate_item(item)
            # print(next_item, f)
            if f & (f < optimal_f):
                optimal_f = f
                optimal_item = next_item.copy()
            item = next_item.copy()

        print('Optimal: ', optimal_item, optimal_f)

    @staticmethod
    def __f(item):
        f_value = 0

        for i in range(len(item)):
            gene = int(item[i])
            if utils.cities[i] <= utils.points[gene]:
                f_value += utils.A[gene][i] + utils.points[gene] - utils.cities[i]
            else:
                return False
        return f_value

    def __generate_item(self, prev_item):
        item = prev_item.copy()

        for i in range(self.__cities_count):
            if prev_item[i] < (self.__points_count - 1):
                item[i] += 1
                break
            else:
                for j in range(self.__cities_count - 1):
                    if item[j + 1] < (self.__points_count - 1):
                        item[j + 1] += 1
                        item[j] = 0
                        return item, self.__f(item)
                    item[j] = 0

        return item, self.__f(item)
