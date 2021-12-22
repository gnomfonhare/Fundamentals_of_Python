with open('new_file_1.txt', 'w') as file:
    user_str = ' '
    while user_str != '':
        user_str = input('Введите следующую строку: ')
        print(user_str, file=file)
