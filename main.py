from players import Player
from weapons import Sword, Axe, Bow, Dagger, Mace
from arenas import TheBattleArena, TheForestArena, TheDesertArena, TheIceArena
import random

def main():
    # Define a list of available weapons with their name and damage
    available_weapons = [
        Sword("Sword", 30),
        Axe("Axe", 35),
        Bow("Bow", 25),
        Dagger("Dagger", 20),
        Mace("Mace", 40)
    ]

    # Define a list of available arenas with their name and description
    available_arenas = [
        TheBattleArena("The Battle Arena", "A gladiatorial arena where heroes and villains clash."),
        TheForestArena("The Forest Arena", "A dense forest where fighters battle amidst trees and foliage."),
        TheDesertArena("The Desert Arena", "A scorching desert where combatants face off under the blazing sun."),
        TheIceArena("The Ice Arena", "A frozen wasteland where warriors duel on slippery ice.")
    ]

    # Create players
    player1 = Player("Hero", 100, 20)
    player2 = Player("Villain", 80, 25)
    
    # Randomly assign weapons to players
    player1_weapon = random.choice(available_weapons)
    player2_weapon = random.choice(available_weapons)
    player1.weapon = player1_weapon
    player2.weapon = player2_weapon

    # Choose a random arena for both players
    chosen_arena = random.choice(available_arenas)

    # Add players to the same arena
    chosen_arena.add_player(player1)
    chosen_arena.add_player(player2)

    # Print out the randomly selected arena for players
    print(f"{player1.name} and {player2.name} are in {chosen_arena.name}: {chosen_arena.description}")

    # Simulate a battle
    winning_weapon = None
    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        if player2.is_alive():
            player2.attack(player1)
        else:
            winning_weapon = player1.weapon.name
            break
        if player1.is_alive():
            player1.attack(player2)
        else:
            winning_weapon = player2.weapon.name
            break

    # Determine the winner
    if player1.is_alive():
        print(f"{player1.name} wins with {winning_weapon}!")
    else:
        print(f"{player2.name} wins with {winning_weapon}!")

if __name__ == "__main__":
    main()
