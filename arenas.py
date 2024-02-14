from abc import ABC

import random

class Arena(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.players = []

    def add_player(self, player):
        if len(self.players) < 2:
            self.players.append(player)
        else:
            print("Arena is already full.")

    def get_opponent(self, player):
        opponents = [p for p in self.players if p != player]
        if opponents:
            return random.choice(opponents)
        else:
            return None

class TheBattleArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class TheForestArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class TheDesertArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class TheIceArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)
