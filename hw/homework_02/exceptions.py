class LowFuelError(Exception):
    """Attempt to start the engine with an empty tank."""
    pass


class NotEnoughFuel(Exception):
    """There is not enough fuel in the tank to cover the required distance."""
    pass


class CargoOverload(Exception):
    """Cargo weight overloaded."""
    pass
