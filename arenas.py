from abc import ABC

class Arena(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def show_players(self):
        print("Players in the arena:")
        for player in self.players:
            print(f"- {player.name}")

class TheBattleArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class ForestArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class DesertArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class IceArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)
