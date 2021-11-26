import pytest
from math import pi
from HW_11Nov2021.src.Circle import Circle


@pytest.mark.parametrize("name, radius", [
    ("c1", -1), ("c2", 0), ("c3", -0.5)
])
def test_circle_exception(name, radius):
    with pytest.raises(ValueError) as e:
        Circle(name, radius)
    assert str(e.value) == "Circle does not exist!"


@pytest.mark.parametrize("name, radius, area", [
    ("c1", 1, pi), ("c2", 5, 25 * pi), ("c3", 10, 100 * pi)
])
def test_circle_area(name, radius, area):
    c = Circle(name, radius)
    assert c.area == area


@pytest.mark.parametrize("name, radius, perimeter", [
    ("c1", 1, 2 * pi), ("c2", 5, 10 * pi), ("c3", 10, 20 * pi)
])
def test_circle_perimeter(name, radius, perimeter):
    c = Circle(name, radius)
    assert c.perimeter == perimeter
