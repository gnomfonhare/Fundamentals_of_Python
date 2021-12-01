my_list = []
a = input('Введите элемент списка: ')
my_list.append(a)
while a != '-1':
    a = input('Введите следующий элемент списка (чтобы окончить введите -1): ')
    if a != '-1':
        my_list.append(a)
for b in my_list:
    c = my_list.index(b)
    if (c + 2) % 2 == 1:
        my_list.insert(c - 1, b)
        my_list.pop (c + 1)
print(my_list)
