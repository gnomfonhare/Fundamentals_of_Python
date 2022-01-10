class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self):
        print('Машина свернула налево')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return(f'Скорость автомобиля: {self.speed}. Превышена допустимая скорость.')
        else:
            return(f'Скорость автомобиля: {self.speed}.')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return(f'Скорость автомобиля: {self.speed}. Превышена допустимая скорость.')
        else:
            return(f'Скорость автомобиля: {self.speed}.')


class PoliceCar(Car):
    pass


auto_1 = TownCar(50, 'red', 'dodge', False)
auto_2 = SportCar(60, 'yellow', 'toyota', False)
auto_3 = WorkCar(45, 'black', 'ford', False)
auto_4 = PoliceCar(60, 'white', 'lada', True)

print(auto_1.color, auto_2.color, auto_3.color, auto_4.color)
print(f'Автомобиль {auto_1.name}. {auto_1.show_speed()}')
print(f'Автомобиль {auto_3.name}. {auto_3.show_speed()}')
auto_2.go()
auto_4.stop()
