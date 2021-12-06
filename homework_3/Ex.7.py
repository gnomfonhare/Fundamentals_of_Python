def int_func(my_str):
    return my_str.title()

my_string = input('Введите строку из слов, разделённых пробелам (нижний регистр): ').split()
for i in my_string:
    print(int_func(i), end=' ')
