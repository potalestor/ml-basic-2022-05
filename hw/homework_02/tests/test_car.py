from exceptions import LowFuelError, NotEnoughFuel
from car import Car
from engine import Engine
import pytest


def test_car_without_engine():
    c = Car(1000, 10, 10)
    assert c.engine == None


def test_car_set_engine():
    c = Car(1000, 10, 10)
    e = Engine(2, 4)
    c.set_engine(e)
    assert c.engine is not None


def test_car_empty_tank():
    c = Car()
    with pytest.raises(LowFuelError) as exception:
        c.start()


def test_car_not_empty_tank():
    c = Car(1000, 10, 10)
    c.start()


def test_car_move_not_enough_fuel():
    c = Car(1000, 10, 10)
    c.start()
    with pytest.raises(NotEnoughFuel):
        c.move(101)


def test_car_move_enough_fuel():
    c = Car(1000, 10, 10)
    c.start()
    c.move(100)
