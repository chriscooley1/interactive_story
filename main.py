from players import Player, Werewolf, Imp, Ogre, Dragon
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

    available_monsters = [
        Werewolf(player_name, 75, 45),
        Imp(player_name, 60, 35),
        Ogre(player_name, 85, 50),
        Dragon(player_name, 200, 65)
    ]
    
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

    # Randomly assign a weapon to the player
    player_weapon = random.choice(available_weapons)
    player.weapon = player_weapon

    # Print out the selected arena, weapon, and opponent for the player
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player_weapon.name}.")

    # Randomly choose between a monster or another player as the opponent
    if random.choice([True, False]):
        # Randomly choose a monster as the opponent
        opponent = random.choice(available_monsters)
    else:
        # Create a random player as the opponent
        opponent_names = ["Werewolf", "Imp", "Ogre", "Dragon"]
        opponent_name = random.choice(opponent_names)
        opponent = Player(opponent_name, 100, 20)

    # Print out the selected arena, weapon, and opponent for the player
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player_weapon.name}.")

    # Check if opponent is a monster or a player and print their information accordingly
    if isinstance(opponent, Player):
        opponent_damage = opponent.attack_power + (opponent.weapon.damage if opponent.weapon else 0)
        print(f"Your opponent is {opponent.name} with {opponent.health} health and {opponent_damage} damage.")
    else:
        print(f"Your opponent is {opponent.name} with {opponent.health} health and {opponent.attack_damage} damage.")

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

    # Initialize damage counters
    player_damage_taken = 0
    opponent_damage_taken = 0

    # Simulate a battle
    while player.is_alive() and opponent.is_alive():
        # Player attacks opponent
        player_attack_damage = player.attack(opponent)
        print(f"You dealt {player_attack_damage} damage to {opponent.name}!")

        # Check if opponent is still alive
        if opponent.is_alive():
            # Opponent counterattacks
            opponent_attack_damage = opponent.attack(player)
            print(f"{opponent.name} dealt {opponent_attack_damage} damage to you!")

            # Track damage taken by both player and opponent
            player_damage_taken += opponent_attack_damage
            opponent_damage_taken += player_attack_damage

        else:
            winning_weapon = player.weapon.name
            break

    # Determine the winner and display damage information
    if winning_weapon is not None:
        print(f"Congratulations, {player.name}! You emerged victorious with {winning_weapon}.")
    else:
        print(f"Unfortunately, you have been defeated. Better luck next time!")

    # Display damage information
    print(f"Total damage dealt to {player.name}: {player_damage_taken}")
    print(f"Total damage dealt to {opponent.name}: {opponent_damage_taken}")


if __name__ == "__main__":
    main()