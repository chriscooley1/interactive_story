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
        if self.weapon is not None:
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
    damage = 50
    print(f"""{player.name} unleashes a terriying Rapid Assault. 
          The player performs a rapid succession of strikes against 
          a single target or multiple nearby enemies, dealing 
          significant damage to {target.name}, dealing {damage} damage!""")
    target.take_damage(damage)
    return damage

def howl_of_despair(player, target):
    damage = 50
    print(f"""{player.name} unleashes a terriying Howl of Despair. 
          The werewolf lets out a terrifying howl that can debuff 
          enemies within a certain radius, reducing their attack 
          power or causing fear, which might make them miss their 
          next attack to {target.name}, dealing {damage} damage!""")
    target.take_damage(damage)
    return damage

def bloodlust(player, target):
    damage = 50
    print(f"""{player.name} unleashes a terriying Bloodlust. 
          With each hit that successfully damages an opponent, 
          the orc gains a small amount of health or a temporary 
          increase in attack power, representing its battle-fueled 
          frenzy to {target.name}, dealing {damage} damage!""")
    target.take_damage(damage)
    return damage

def berserker_strike(player, target):
    damage = 50
    print(f"""{player.name} unleashes a terriying Berserker Strike. 
          The ogre unleashes a series of powerful blows, each hit 
          dealing increased damage. This could involve swinging a 
          massive weapon or using brute force to pummel the enemy to 
          {target.name}, dealing {damage} damage!""")
    target.take_damage(damage)
    return damage

def dragons_breath(player, target):
    damage = 50
    print(f"""{player.name} unleashes a terriying Dragon's Breath. 
          The dragon unleashes its ancient, elemental power in a 
          devastating breath attack that not only causes direct damage 
          but also alters the battlefield in a significant way to 
          {target.name}, dealing {damage} damage!""")
    target.take_damage(damage)
    return damage

def bone_shield(player, target):
    damage = 50
    print(f"""{player.name} unleashes a terriying Bone Shield. 
          As the bones fly out, some of them circle back to form 
          a temporary shield around the skeleton, providing a defensive 
          buff or absorbing a certain amount of damage from incoming 
          attacks to {target.name}, dealing {damage} damage!""")
    target.take_damage(damage)
    return damage

def plague_swarm(player, target):
    damage = 50
    print(f"""{player.name} unleashes a terriying Plague Swarm. 
          The zombie unleashes a virulent, contagious plague that 
          not only damages but also has a chance to infect enemies, 
          potentially turning them into weaker zombie minions to 
          {target.name}, dealing {damage} damage!""")
    target.take_damage(damage)
    return damage

class Hero(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)

class FierceWerewolf(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)

class MightyOrc(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)

class GiantOgre(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)

class AncientDragon(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)
    
class CreepySkeleton(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)
    
class ScaryZombie(Player):
    def __init__(self, name, health, attack_power, special_attack_function, weapon=None):
        super().__init__(name, health, attack_power, weapon)
        self._special_attack = special_attack_function

    def special_attack(self, target):
        return self._special_attack(self, target)