from abc import ABC

class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
