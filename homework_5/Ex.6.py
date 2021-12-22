with open('new_file_6.txt') as file:
    content = file.readlines()
    result_dict = {}
    for el in content:
        el = el.replace(':', '')
        cont = [int(elem) for elem in el.split(' ') if elem.isdigit()]
        result_dict[el.split(' ')[0]] = sum(cont)
    print(result_dict)
