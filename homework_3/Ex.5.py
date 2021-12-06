def int_func(num_str, stop):
    nums_list = num_str.split(' ')
    result = 0
    for i in nums_list:
        if i == stop:
            break
        result += int(i)
    return result


stopper = '$'
finished = False
s = 0

while not finished:
    num_str_user = input('Введите набор чисел, разделённых пробелом (чтобы закончить, введите $): ')
    s += int_func(num_str_user, stopper)
    finished = stopper in num_str_user
    print(f'Сумма введённых чисел: {s}')
