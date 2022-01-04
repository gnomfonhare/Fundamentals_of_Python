class Date:
    list_date = None
    int_day = None
    int_month = None
    int_year = None

    def __init__(self, date):
        Date.list_date = date.split('-')

    @classmethod
    def int_date(cls):
        a = cls.list_date
        cls.int_day = int(a[0])
        cls.int_month = int(a[1])
        cls.int_year = int(a[2])
        cls.list_date = (cls.int_day, cls.int_month, cls.int_year)
        return cls.list_date

    @staticmethod
    def val_date(date):
        num_days_31 = (1, 3, 5, 7, 8, 10, 12)
        num_days_30 = (4, 6, 9, 11)
        if date[1] > 12 or date[2] % 4 == 0 and date[1] == 2 and date[0] > 29\
                or date[2] % 4 > 0 and date[1] == 2 and date[0] > 28\
                or date[1] in num_days_31 and date[0] > 31\
                or date[1] in num_days_30 and date[0] > 30:
            return 'Введена неверная дата.'
        else:
            return 'Введена верная дата.'


my_date = Date(input('Введите дату в формате "день-месяц-год": '))
print(my_date.int_date())
print(my_date.val_date(my_date.int_date()))
