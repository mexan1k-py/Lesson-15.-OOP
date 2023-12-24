#Homework 1
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):                    #Homework 2
        return f'Вместимость одного автобуса {self.name}: '\
               f'{capacity} пассажиров'

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self):                              #Homework 2
        return super().seating_capacity(capacity = 50)

    def __str__(self):
        return  f'Название автомобиля: {autobus.name}, '\
                f'Скорость: {autobus.max_speed}, '\
                f'Пробег: {autobus.mileage}.'

autobus = Autobus('Renault Logan', 180, 12)
print(autobus)
print(autobus.seating_capacity()) #Homework 2

