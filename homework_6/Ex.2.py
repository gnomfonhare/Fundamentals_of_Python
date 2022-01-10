class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_calculation(self, a, b):
        return(self._lenght * self._width * a * b / 1000)


my_road = Road(5000, 20)
print(f'{my_road.mass_calculation(25, 5)}т')
