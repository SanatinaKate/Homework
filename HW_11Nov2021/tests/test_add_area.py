import pytest
from math import pi
from HW_11Nov2021.src.Circle import Circle
from HW_11Nov2021.src.Rectangle import Rectangle
from HW_11Nov2021.src.Square import Square
from HW_11Nov2021.src.Triangle import Triangle


class A:
    pass


a = A()
c = Circle("c", 1)
r = Rectangle("r", 3, 4)
s = Square("s", 10)
t = Triangle("t", 13, 14, 15)


@pytest.mark.parametrize("figure", [c, r, s, t])
def test_incorrect_class(figure):
    with pytest.raises(ValueError) as e:
        figure.add_area(a)
    assert str(e.value) == "Can not add area because argument has incorrect class"


def test_total_area():
    assert c.add_area(r) + s.add_area(t) == r.add_area(s) + t.add_area(c) == pi + 196
