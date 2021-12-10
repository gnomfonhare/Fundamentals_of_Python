my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 301]
print([i for i in my_list if i > my_list[my_list.index(i) - 1] and my_list.index(i) != 0])
