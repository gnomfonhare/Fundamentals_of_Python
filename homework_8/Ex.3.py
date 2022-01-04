class MyException(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
a = None
while a != 'stop':
    a = input('Введите элемент списка - только числа добавятся в'
              ' список (чтобы окончить введите "stop"): ')
    try:
        if a != 'stop' and a.isdigit():
            my_list.append(int(a))
            print(my_list)
        elif a != 'stop' and not a.isdigit():
            raise MyException('В список можно добавить только число.')
        elif a == 'stop':
            break
    except MyException as e:
        print(e)
        print(my_list)
