class Matrix:
    def __init__(self, m_str):
        self.m_str = m_str

    def __add__(self, other):
        a = self.m_str
        b = other.m_str
        result_str = [[a[i][j] + b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
        result = ''
        for i in result_str:
            for j in i:
                result += f'{j:02} '
            result += '\n'
        return result

    def __str__(self):
        result = ''
        for i in self.m_str:
            for j in i:
                result += f'{j:02} '
            result += '\n'
        return result


mm_1 = Matrix([[1, 2, 3, 4, 5], [4, 3, 2, 1, 5], [1, 2, 3, 4, 5]])
mm_2 = Matrix([[4, 3, 2, 1, 5], [1, 2, 3, 4, 4], [4, 3, 2, 1, 3]])
print(mm_1)
print(mm_2)
print(mm_1 + mm_2)
