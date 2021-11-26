from math import pi
from HW_11Nov2021.src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        if radius <= 0:
            raise ValueError("Circle does not exist!")
        self.name = name
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius * self.radius

    @property
    def perimeter(self):
        return 2 * pi * self.radius
