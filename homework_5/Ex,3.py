with open('new_file_3.txt') as file:
    content = file.readlines()
    loosers = []
    summ_cash = 0
    num_str = 0
    for el in content:
        num_str += 1
        string = el.split(' ')
        if int(string[1]) < 20000:
            loosers.append(string[0])
        summ_cash += int(string[1])
    mid_cash = summ_cash / num_str
    print(f'Работники с доходом менее 20к: {loosers}.')
    print(f'Средний доход сотрудников: {mid_cash}')
