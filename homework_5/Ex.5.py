with open('new_file_5.txt', 'w+') as file:
    for el in range(1, 11):
        print(el, end=' ', file=file)
    file.seek(0)
    content = file.read()
    cont = content.split(' ')
    n = 0
    for el in cont:
        if el.isdigit():
            n += int(el)
    print(n)
