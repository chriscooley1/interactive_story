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
        return damage_dealt
    
    @abstractmethod
    def special_attack(self, target):
        "Perform special attack"
        pass

def rapid_assualt(player, target):
    # Implementation of the Werewolf's special attack
    damage = 30  # Example damage value
    print(f"{player.name} uses Howl on {target.name}!")
    target.take_damage(damage)
    return damage

def howl_of_despair(player, target):
    # Implementation of the Werewolf's special attack
    damage = 30  # Example damage value
    print(f"{player.name} uses Howl on {target.name}!")
    target.take_damage(damage)
    return damage

def bloodlust(player, target):
    # Implementation of the Werewolf's special attack
    damage = 30  # Example damage value
    print(f"{player.name} uses Howl on {target.name}!")
    target.take_damage(damage)
    return damage

def berserker_strike(player, target):
    # Implementation of the Werewolf's special attack
    damage = 30  # Example damage value
    print(f"{player.name} uses Howl on {target.name}!")
    target.take_damage(damage)
    return damage

def dragons_breath(player, target):
    # Implementation of the Werewolf's special attack
    damage = 30  # Example damage value
    print(f"{player.name} uses Howl on {target.name}!")
    target.take_damage(damage)
    return damage

def bone_shield(player, target):
    # Implementation of the Werewolf's special attack
    damage = 30  # Example damage value
    print(f"{player.name} uses Howl on {target.name}!")
    target.take_damage(damage)
    return damage

def plague_swarm(player, target):
    # Implementation of the Werewolf's special attack
    damage = 30  # Example damage value
    print(f"{player.name} uses Howl on {target.name}!")
    target.take_damage(damage)
    return damage

class Hero(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)
    
class Werewolf(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)

class Orc(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)

class Ogre(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)

class Dragon(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)
    
class Skeleton(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)
    
class Zombie(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)