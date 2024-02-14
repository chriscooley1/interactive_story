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
    player_name = input("Enter your character's name: ")
    player = Player(player_name, 100, 20)
    
    # Randomly assign a weapon to the player
    player_weapon = random.choice(available_weapons)
    player.weapon = player_weapon

    # Choose a random arena for the player
    chosen_arena = random.choice(available_arenas)

    # Add the player to the chosen arena
    chosen_arena.add_player(player)

    # Print out the selected arena and weapon for the player
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player_weapon.name}.")

    # Simulate the interactive story based on the chosen arena
    if isinstance(chosen_arena, TheBattleArena):
        print("As you enter the gladiatorial arena, the crowd roars with excitement. The atmosphere is charged with tension.")
        # Add more narrative specific to TheBattleArena
    elif isinstance(chosen_arena, TheForestArena):
        print("You find yourself in a dense forest, surrounded by towering trees and mysterious sounds. The air is filled with the scent of nature.")
        # Add more narrative specific to TheForestArena
    elif isinstance(chosen_arena, TheDesertArena):
        print("The scorching sun beats down on the endless expanse of the desert. The heat is almost unbearable, and the sand stretches as far as the eye can see.")
        # Add more narrative specific to TheDesertArena
    elif isinstance(chosen_arena, TheIceArena):
        print("You stand on a frozen wasteland, the icy ground beneath your feet. The air is bone-chilling, and the sound of cracking ice echoes in the distance.")
        # Add more narrative specific to TheIceArena

    # Initialize winning_weapon outside the battle loop
    winning_weapon = None

    # Simulate a battle
    while player.is_alive():
        opponent = chosen_arena.get_opponent(player)
        if opponent is not None:
            player.attack(opponent)
            if opponent.is_alive():
                opponent.attack(player)
            else:
                winning_weapon = player.weapon.name
                break
        else:
            print("No opponents available in the arena.")
            break

    # Determine the winner
    if winning_weapon is not None:
        print(f"Congratulations, {player.name}! You emerged victorious with {winning_weapon}.")
    else:
        print("Unfortunately, you have been defeated. Better luck next time!")


if __name__ == "__main__":
    main()
