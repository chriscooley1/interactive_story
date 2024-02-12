from players import Player
from weapons import Weapon
from arenas import Arena
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

    #Define a list of available arenas with their name and description
    available_arenas = [
        {"name": "The Battle Arena", "description": "A gladiatorial arena where heroes and villains clash."},
        {"name": "Forest Arena", "description": "A dense forest where fighters battle amidst trees and foliage."},
        {"name": "Desert Arena", "description": "A scorching desert where combatants face off under the blazing sun."},
        {"name": "Ice Arena", "description": "A frozen wasteland where warriors duel on slippery ice."}
    ]

    # Create players
    player1 = Player("Hero", 100, 20)
    player2 = Player("Villain", 80, 25)
    
    # Randomly assign weapons to players
    player1_weapon = Weapon(**random.choice(available_weapons))
    player2_weapon = Weapon(**random.choice(available_weapons))
    player1.weapon = player1_weapon
    player2.weapon = player2_weapon


    player1_arena = Arena(**random.choice(available_arenas))
    player2_arena = Arena(**random.choice(available_arenas))
    player1.arena = player1_arena
    player2.arena = player2_arena

    # Add players to the arena
    Arena("", "").add_player(player1)
    Arena("", "").add_player(player2)

    # Show players in the arena
    Arena("", "").show_players()

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
