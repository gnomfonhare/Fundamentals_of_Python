class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return(f'{self.name} {self.surname}')

    def get_total_income(self):
        return(sum(self._income.values()))


worker_1 = Position('Иван', 'Иванов', 'Повар', {"wage": 50000, "bonus": 5000})
worker_2 = Position('Пётр', 'Петров', 'Уборщик', {"wage": 30000, "bonus": 3000})
print(f'{worker_1.get_full_name()} {worker_1.get_total_income()}')
print(f'{worker_2.get_full_name()} {worker_2.get_total_income()}')
