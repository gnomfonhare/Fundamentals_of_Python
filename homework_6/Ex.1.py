import time

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'красный':
            print(f'Горит {self.__color} свет')
            time.sleep(7)
            self.__color = 'жёлтый'
            print(f'Горит {self.__color} свет')
            time.sleep(2)
            self.__color = 'зелёный'
            print(f'Горит {self.__color} свет')
            time.sleep(5)
        else:
            print('Нарушен порядок режимов')


my_traffic_light = TrafficLight('красный')
my_traffic_light.running()
