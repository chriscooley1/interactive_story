from abc import ABC

class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Sword(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Axe(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Bow(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Dagger(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Mace(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)