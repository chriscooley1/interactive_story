from players import Player
from weapons import Weapon
from arenas import TheBattleArena, ForestArena, DesertArena, IceArena
import random

def main():
    # Define a list of available weapons with their name and damage
    available_weapons = [
        {"name": "Sword", "damage": 30},
        {"name": "Axe", "damage": 35},
        {"name": "Bow", "damage": 25},
        {"name": "Dagger", "damage": 20},
        {"name": "Mace", "damage": 40}
    ]

    # Create players
    player1 = Player("Hero", 100, 20)
    player2 = Player("Villain", 80, 25)
    
    # Randomly assign weapons to players
    player1_weapon = Weapon(**random.choice(available_weapons))
    player2_weapon = Weapon(**random.choice(available_weapons))
    player1.weapon = player1_weapon
    player2.weapon = player2_weapon

    # Choose a random arena for both players
    arena_classes = [TheBattleArena, ForestArena, DesertArena, IceArena]
    chosen_arena_class = random.choice(arena_classes)
    chosen_arena = chosen_arena_class(chosen_arena_class.__name__, chosen_arena_class.__doc__)


    # Add players to the same arena
    chosen_arena.add_player(player1)
    chosen_arena.add_player(player2)

    # Print out the randomly selected arena for players
    print(f"{player1.name} and {player2.name} are in {chosen_arena.name}: {chosen_arena.description}")

    # Simulate a battle
    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        player2.attack(player1)

    # Determine the winner
    if player1.is_alive():
        print(f"{player1.name} wins!")
    else:
        print(f"{player2.name} wins!")

if __name__ == "__main__":
    main()
