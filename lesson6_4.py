#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
#что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
#TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
#который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
#При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self,speed,color,name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self,direction):
        if direction == "left":
            print("Машина повернула налево")
        elif direction == "right":
            print("Машина повернула направо")
        else:
            print("Машина повернула, но это не точно")
    def show_speed(self):
        print("Скорость автомобиля: "+str(self.speed))

class SportCar(Car):
    def __init__(self,speed,color,name):
        super().__init__(speed,color,name)

class TownCar(Car):
    def __init__(self,speed,color,name):
        super().__init__(speed,color,name)
    def show_speed(self):
        print("Скорость автомобиля: "+str(self.speed))
        if int(self.speed) > 60:
            print("Скорость превышена")

class WorkCar(Car):
    def __init__(self,speed,color,name):
        super().__init__(speed,color,name)
    def show_speed(self):
        print("Скорость автомобиля: "+str(self.speed))
        if int(self.speed) > 40:
            print("Скорость превышена")

class PoliceCar(Car):
    is_police = True
    def __init__(self,speed,color,name):
        super().__init__(speed,color,name)

car1 = TownCar(100,"red","car1")
print(car1.name)
car1.go()
car1.stop()
car1.turn("left")
print(car1.color)
car1.show_speed()
print(car1.is_police)

car2 = SportCar("120","White","car2")
print(car2.name)
car2.turn("omg it's Ferrari")

car3 = PoliceCar("110","Police_colors","car3")
print(car3.name)
car3.show_speed()
print(car3.is_police)

car4 = WorkCar("30","Black", "car4")
print(car4.name)
car4.show_speed()
