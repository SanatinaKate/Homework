from HW_11Nov2021.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle does not exist!")
        self.name = name
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2
