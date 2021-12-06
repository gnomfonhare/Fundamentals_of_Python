def my_func(name, famy, date, city, mail, phone):
    return f'{name} {famy} {date} {city} {mail} {phone}'


a = input('Введите имя: ')
b = input('Введите фамилию: ')
c = input('Введите год рождения: ')
d = input('Введите город проживания: ')
e = input('Введите введите e-mail: ')
f = input('Введите телефон: ')

print(my_func(name=a, famy=b, date=c, city=d, mail=e, phone=f))
