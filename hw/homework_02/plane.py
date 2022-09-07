from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0.0, fuel=0.0, fuel_consumption=0.0, max_cargo=0):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.__max_cargo = max_cargo
        self.__cargo = 0
    
    def load_cargo(self, cargo):
        if (self.__cargo + cargo > self.__max_cargo):
            raise CargoOverload
        self.__cargo += cargo
    
    def remove_all_cargo(self):
        old_cargo = self.__cargo
        self.__cargo = 0
        return old_cargo