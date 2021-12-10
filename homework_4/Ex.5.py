from functools import reduce


my_list = [i for i in range(100, 1001)]
print(reduce(lambda prev, cur: prev * cur, my_list))
