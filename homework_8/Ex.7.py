class ComplexNumber:
    def __init__(self, valid_part, im_part):
        self.valid_part = valid_part
        self.im_part = im_part

    def __str__(self):
        if self.im_part < 0:
            return f'{self.valid_part}{self.im_part}i'
        else:
            return f'{self.valid_part}+{self.im_part}i'

    def __add__(self, other):
        return ComplexNumber(self.valid_part + other.valid_part, self.im_part + other.im_part)

    def __mul__(self, other):
        a1 = self.valid_part
        a2 = other.valid_part
        b1 = self.im_part
        b2 = other.im_part
        return ComplexNumber(a1 * a2 - b1 * b2, a1 * b2 + b1 * a2)


cn_1 = ComplexNumber(6, 6)
cn_2 = ComplexNumber(2, -3)
print(f'Первое комплексное число: {cn_1}')
print(f'Второе комплексное число: {cn_2}')
print(f'Сумма комплексных чисел: {cn_1 + cn_2}')
print(f'Произведение комплексных чисел: {cn_1 * cn_2}')
