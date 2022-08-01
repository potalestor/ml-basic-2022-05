from dataclasses import dataclass


@dataclass
class Engine:
    """
    Engine.

    Attributes:
        volume
        pistons
    """
    volume: int
    pistons: int
