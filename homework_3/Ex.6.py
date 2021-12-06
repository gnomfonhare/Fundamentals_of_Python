def int_func(my_str):
    return my_str.title()


my_string = input('Введите слово (нижний регистр): ')
if ' ' in my_string:
    print('Строка не соответствует условию')
else:
    print(int_func(my_string))
