from itertools import cycle, count


user_start = int(input('Введите целое число от 0 до 10: '))
my_counter = count(user_start, 1)
for i in range(11 - user_start):
    print(next(my_counter))

user_stop = int(input('Сколько раз повторить элементы предопределённого списка? Введите целое число: '))
my_list = ['a', 'b', 'c']
my_cycle = cycle(my_list)
for j in range((user_stop)):
    print(next(my_cycle))
