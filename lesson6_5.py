#5. Реализовать класс Stationery (канцелярская принадлежность).
#Определить в нем атрибут title (название) и метод draw (отрисовка).
#Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
#Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
#Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
#что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Рисуем ручкой")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Рисуем карандашом")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Рисуем маркером")

var1 = Stationery("Feather")
var1.draw()
var2 = Pen("Pen")
var2.draw()
var3 = Pencil("Pencil")
var3.draw()
var4 = Handle("Handle")
var4.draw()
