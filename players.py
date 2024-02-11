from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, health, attack_power, weapon=None):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapon = weapon

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, target):
        if self.weapon:
            damage_dealt = self.attack_power + self.weapon.damage
        else:
            damage_dealt = self.attack_power
        target.take_damage(damage_dealt)
