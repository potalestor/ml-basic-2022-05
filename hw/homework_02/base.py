from exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    """
    Vehicle is a base class.

    Attributes:
        weight - weight in kilograms
        fuel - amount of fuel in liters
        fuel_consumption - l/100 km

    Methods:
        start(self) - starts engine
        start(self, distance) - starts engine
    """

    def __init__(self, weight=0.0, fuel=0.0, fuel_consumption=0.0):
        self.__weight = weight
        self.__fuel = fuel
        self.__fuel_consumption = fuel_consumption
        self.__started = False

    def start(self):
        """
        Raises:
            LowFuelError if tank is empty
        """
        if not self.__started:
            if self.__fuel == 0:
                raise LowFuelError

            self.__started = True

    def move(self, distance):
        """
        Parameters:
            distance in km

        Raises:
            NotEnoughFuel if not enough fuel for the distance
        """
        required_fuel = self.__fuel_consumption * distance / 100
        if required_fuel > self.__fuel:
            raise NotEnoughFuel(required_fuel, self.__fuel)
        self.__fuel -= required_fuel
