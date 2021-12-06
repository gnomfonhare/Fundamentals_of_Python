def my_div (arg_1, arg_2):
    if arg_2 != 0:
        result = arg_1 / arg_2
        if result - int(result) == 0:
            return int(result)
        else:
            return result
    else:
        result = 'На ноль делить нельзя'
        return result


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))

print(my_div(a, b))
