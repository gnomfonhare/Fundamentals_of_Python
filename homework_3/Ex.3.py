def sum_max_arg(arg_1, arg_2, arg_3):
    my_tup = (arg_1, arg_2, arg_3)
    result = sum(my_tup) - min(my_tup)
    if result - int(result) == 0:
        return int(result)
    else:
        return result


a = float(input('Введите первый аргумент: '))
b = float(input('Введите второй аргумент: '))
c = float(input('Введите третий аргумент: '))

print(f'Сумма двух наибольших аргументов: {sum_max_arg(a, b, c)}')
