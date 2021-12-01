a = input('Введите строку из нескольких слов, разделённых пробелами: ').split()
for ind, el in enumerate(a, 1):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(f"{ind} - {el[:10]})
