import pytest
from HW_11Nov2021.src.Square import Square


@pytest.mark.parametrize("name, a", [
    ("s1", -1), ("s2", 0), ("s3", -0.5)
])
def test_square_exception(name, a):
    with pytest.raises(ValueError) as e:
        Square(name, a)
    assert str(e.value) == "Square does not exist!"


@pytest.mark.parametrize("name, a, area", [
    ("s1", 1, 1), ("s2", 5, 25), ("s3", 10, 100)
])
def test_square_area(name, a, area):
    s = Square(name, a)
    assert s.area == area


@pytest.mark.parametrize("name, a, perimeter", [
    ("s1", 1, 4), ("s2", 5, 20), ("s3", 10, 40)
])
def test_square_perimeter(name, a, perimeter):
    s = Square(name, a)
    assert s.perimeter == perimeter
