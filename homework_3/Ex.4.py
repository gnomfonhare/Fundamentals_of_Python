def my_func(x, y):
    # return x ** y
    z = 1
    for i in range(-y):
        z *= x
    return 1 / z

a = float(input('Введите действительное положительное число (основание степени): '))
b = int(input('Введите целое отрицательное число (показатель степени): '))

if a <= 0 or b >= 0:
    print('Введены неверные числа')
else:
    print(my_func(a, b))
