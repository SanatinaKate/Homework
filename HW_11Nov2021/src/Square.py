from HW_11Nov2021.src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, a):
        if a <= 0:
            raise ValueError("Square does not exist!")
        super().__init__(name, a, a)
