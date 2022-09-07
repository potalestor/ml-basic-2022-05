from exceptions import CargoOverload
from plane import Plane
import pytest

def test_plane_load_cargo():
    p = Plane(1000, 10, 10, 10000)
    p.load_cargo(10000)
    with pytest.raises(CargoOverload):
        p.load_cargo(1)

def test_plane_load_cargo():
    p = Plane(1000, 10, 10, 10000)
    p.load_cargo(10000)

    assert p.remove_all_cargo() == 10000