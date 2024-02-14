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

class TheForestArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class TheDesertArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)

class TheIceArena(Arena):
    def __init__(self, name, description):
        super().__init__(name, description)
