#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage,"bonus":bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name
    def get_total_income(self):
        total_income = int(self._income.get("wage")) + int(self._income.get("bonus"))
        return total_income

Seller = Position("Vasiliy","Pupkin","Seller","30000","5000")
Manager = Position("Petr","Volkov","Manager", 60000, 20000)

print (Seller.get_full_name())
print (Seller.get_total_income())
print (Manager.get_full_name())
print (Manager.get_total_income())
