def fact(n):
    mul_nums = 1
    for i in range(1, n + 1):
        mul_nums *= i
        yield mul_nums


user_n = int(input('Введите целое положительное число: '))
for el in fact(user_n):
    print(el)
