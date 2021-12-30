class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

    def __sub__(self, other):
        subtraction = self.num_cells - other.num_cells
        if subtraction <= 0:
            return 'Ошибка вычитания.'
        else:
            return Cell(subtraction)

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __truediv__(self, other):
        return Cell(self.num_cells // other.num_cells)

    def make_order(self, count):
        a = ''
        for i in range(self.num_cells // count):
            a += '*' * count + '\n'
        a += '*' * (self.num_cells % count) + '\n'
        return a

    def __str__(self):
        return f'{self.num_cells}'


cell_1 = Cell(30)
cell_2 = Cell(20)
print(cell_1.make_order(10))
print(cell_2.make_order(11))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print((cell_1 + cell_2).make_order(10))
