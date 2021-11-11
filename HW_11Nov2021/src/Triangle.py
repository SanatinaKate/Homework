from math import sqrt
from HW_11Nov2021.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle does not exist!")
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        p = (self.a + self.b + self.c)/2
        result = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        if result.is_integer():
            result = int(result)
        return result

    @property
    def perimeter(self):
        return self.a + self.b + self.c
