#2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
#для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
#реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, var):
        self.var = var
    @abstractmethod
    def count_cloth(self):
        pass

class Coat(Cloth):
    def __init__(self,var):
        self.var = var
    @property
    def count_cloth(self,):
        return self.var / 6.5 + 0.5

class Suit(Cloth):
    def __init__(self,var):
        self.var = var
    @property
    def count_cloth(self):
        return 2 * self.var + 0.3

a = Coat(48)
b = Suit(1.78)
c = Suit(1.50)
print(a.count_cloth)
print(b.count_cloth)
print(c.count_cloth)
print(a.count_cloth * 5 + b.count_cloth * 3)
