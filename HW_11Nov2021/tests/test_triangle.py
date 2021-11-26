import pytest
from math import sqrt
from HW_11Nov2021.src.Triangle import Triangle


@pytest.mark.parametrize("name, a, b, c", [
    ("t1", -1, 1, 2), ("t2", 1, 0, 2), ("t3", 1, 2, -2), ("t4", -1, -2, -3), ("t5", 1, 2, 3), ("t6", 10, 5, 3)
])
def test_triangle_exception(name, a, b, c):
    with pytest.raises(ValueError) as e:
        Triangle(name, a, b, c)
    assert str(e.value) == "Triangle does not exist!"


@pytest.mark.parametrize("name, a, b, c, area", [
    ("t1", 1, 1, 1, sqrt(3)/4), ("t2", 3, 4, 5, 6), ("t3", 13, 14, 15, 84)
])
def test_triangle_area(name, a, b, c, area):
    t = Triangle(name, a, b, c)
    assert t.area == area


@pytest.mark.parametrize("name, a, b, c, perimeter", [
    ("t1", 1, 1, 1, 3), ("t2", 3, 4, 5, 12), ("t3", 13, 14, 15, 42)
])
def test_triangle_perimeter(name, a, b, c, perimeter):
    t = Triangle(name, a, b, c)
    assert t.perimeter == perimeter
