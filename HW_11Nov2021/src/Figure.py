class Figure:
    name = None

    @property
    def area(self):
        raise NotImplemented("Property area should be implemented")

    @property
    def perimeter(self):
        raise NotImplemented("Property perimeter should be implemented")

    def add_area(self, other):
        if not isinstance(other, Figure):
            raise ValueError("Can not add area because argument has incorrect class")
        return self.area + other.area
