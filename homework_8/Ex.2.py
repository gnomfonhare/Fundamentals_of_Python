class MyException(Exception):
    def __init__(self, text):
        self.text = text


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))
try:
    if b == 0:
        raise MyException('На 0 делить нельзя.')
    else:
        print(a / b)
except MyException as e:
    print(e)
