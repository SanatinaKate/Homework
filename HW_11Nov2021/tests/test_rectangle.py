import pytest
from HW_11Nov2021.src.Rectangle import Rectangle


@pytest.mark.parametrize("name, a, b", [
    ("r1", -1, 1), ("r2", 0, 1), ("r3", 1, -1), ("r4", 1, 0), ("r5", -1, -1)
])
def test_rectangle_exception(name, a, b):
    with pytest.raises(ValueError) as e:
        Rectangle(name, a, b)
    assert str(e.value) == "Rectangle does not exist!"


@pytest.mark.parametrize("name, a, b, area", [
    ("r1", 1, 1, 1), ("r2", 4, 5, 20), ("r3", 10, 20, 200)
])
def test_rectangle_area(name, a, b, area):
    r = Rectangle(name, a, b)
    assert r.area == area


@pytest.mark.parametrize("name, a, b, perimeter", [
    ("r1", 1, 1, 4), ("r2", 4, 5, 18), ("r3", 10, 20, 60)
])
def test_rectangle_perimeter(name, a, b, perimeter):
    r = Rectangle(name, a, b)
    assert r.perimeter == perimeter
