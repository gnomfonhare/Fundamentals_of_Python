class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return(f'{self.name} {self.surname}')

    def get_total_income(self):
        return(sum(self._income.values()))


worker_1 = Position('Иван', 'Иванов', 'Повар', 50000, 5000)
worker_2 = Position('Пётр', 'Петров', 'Уборщик', 30000, 3000)
print(f'{worker_1.get_full_name()} {worker_1.get_total_income()}')
print(f'{worker_2.get_full_name()} {worker_2.get_total_income()}')
