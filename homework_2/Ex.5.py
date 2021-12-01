r = [8, 7, 5, 3, 1]
print(f'Изначальный набор натуральных чисел: {r}')
a = 0
while a != -1:
    a = int(input('Введите следующее число для интеграции в "рейтинг" (чтобы закончить, введите -1): '))
    for el in r:
        if a < r[-1]:
            r.append(a)
            print(r)
            break
        elif el < a:
            r.insert(0, a)
            print(r)
            break
        elif el > a:
            continue
        elif el == a:
            b = r.count(el)
            c = r.index(el)
            if b == 0:
                r.insert(c + 1, a)
                print(r)
                break
            else:
                r.insert(c + b, a)
                print(r)
                break
