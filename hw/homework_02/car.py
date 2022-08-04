from base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self, weight=0.0, fuel=0.0, fuel_consumption=0.0):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
