with open('new_file_4_1.txt') as file:
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    content = file.readlines()
    for el in content:
        cont = el.split(' - ')
        cont1 = cont[0].replace(cont[0], my_dict.get(cont[0]))
        cont2 = f'{cont1} - {cont[1]}'
        with open('new_file_4_2.txt', 'a') as file_1:
            print(cont2, end='', file=file_1)
