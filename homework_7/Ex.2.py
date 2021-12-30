from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def count(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def count(self):
        return 2 * self.h + 0.3

    def sum_count(self, list_costumes):
        a = 0
        for i in list_costumes:
            a += i.count
        return a


my_coat = Coat(52)
my_costume_1 = Costume(1.85)
my_costume_2 = Costume(1.76)
list_costumes = [my_costume_1, my_costume_2]
print(my_coat.count)
print(my_costume_1.count)
print(my_costume_2.count)
print(my_costume_1.sum_count(list_costumes))
