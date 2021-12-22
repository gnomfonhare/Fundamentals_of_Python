with open('new_file_2.txt') as file:
    content = file.readlines()
    strings = 0
    for el in content:
        strings += 1
        words = 0
        cont = el.split(' ')
        for elem in cont:
            words += 1
        print(f'В {strings} строке {words} слов.')
    print(f'Всего в файле {strings} строк.')
