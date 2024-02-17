from players import Player, Hero, Werewolf, Orc, Ogre, Dragon, Skeleton, Zombie, rapid_assualt, howl_of_despair, bloodlust, berserker_strike, dragons_breath, bone_shield, plague_swarm
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
    player = Hero(player_name, 100, 25, rapid_assualt)

    # Create available monsters with appropriate names
    available_monsters = [
        Werewolf("Fierce Werewolf", 75, 45, howl_of_despair),
        Orc("Mighty Orc", 60, 35, bloodlust),
        Ogre("Giant Ogre", 85, 50, berserker_strike),
        Dragon("Ancient Dragon", 200, 65, dragons_breath),
        Skeleton("Creepy Skeleton", 50, 30, bone_shield),
        Zombie("Scary Zombie", 55, 40, plague_swarm)
    ]

    # Create a mapping of opponent classes to their special attacks
    special_attacks_mapping = {
        Werewolf: howl_of_despair,
        Orc: bloodlust,
        Ogre: berserker_strike,
        Dragon: dragons_breath,
        Skeleton: bone_shield,
        Zombie: plague_swarm
    }

    # List of all opponent classes
    opponent_classes = list(special_attacks_mapping.keys())

    # Choose a random arena for the player and the opponent
    chosen_arena = random.choice(available_arenas)
    chosen_arena.add_player(player)  # Add the player to the chosen arena

    # Create an opponent
    if random.choice([True, False]):
        # Randomly choose a monster as the opponent
        opponent = random.choice(available_monsters)
    else:
        # Create a random player as the opponent
        opponent_class = random.choice(opponent_classes)
        opponent_special_attack = special_attacks_mapping[opponent_class]
        opponent_name = f"{opponent_class.__name__}"
        opponent = opponent_class(opponent_name, 100, 20, opponent_special_attack)

    chosen_arena.add_player(opponent)  # Add the opponent to the same arena

    # Randomly assign a weapon to the player
    player_weapon = random.choice(available_weapons)
    player.weapon = player_weapon

    # Print out the selected arena, weapon, and opponent for the player
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player_weapon.name}.")
    print(f"Your opponent is {opponent.name}, entering the {chosen_arena.name}.")

    # Randomly choose between a monster or another player as the opponent
    if random.choice([True, False]):
        # Randomly choose a monster as the opponent
        opponent = random.choice(available_monsters)
    else:
        # Create a random player as the opponent
        opponent_classes = [Werewolf, Orc, Ogre, Dragon, Skeleton, Zombie]
        opponent_class = random.choice(opponent_classes)
        opponent = opponent_class(opponent_class.__name__, 100, 20, rapid_assualt)

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

    def should_use_special_attack(player, opponent):
    # Example condition: use special attack randomly
        return random.choice([True, False])

    # Simulate a battle
    while player.is_alive() and opponent.is_alive():
        # Initialize attack damages for this turn
        player_attack_damage = 0
        opponent_attack_damage = 0

        # Player's turn
        if should_use_special_attack(player, opponent):
            player_attack_damage = player.special_attack(opponent)
            print(f"{player.name} used a special attack on {opponent.name}, dealing {player_attack_damage} damage!")
        else:
            # Regular attack
            player_attack_damage = player.attack(opponent)
            print(f"{player.name} attacked {opponent.name}, dealing {player_attack_damage} damage!")

        # Check if opponent is still alive for their turn
        if opponent.is_alive():
            # Opponent's turn
            if should_use_special_attack(opponent, player):
                opponent_attack_damage = opponent.special_attack(player)
                print(f"{opponent.name} used a special attack on {player.name}, dealing {opponent_attack_damage} damage!")
            else:
                # Regular attack
                opponent_attack_damage = opponent.attack(player)
                print(f"{opponent.name} attacked {player.name}, dealing {opponent_attack_damage} damage!")

        # Track damage taken by both player and opponent
        player_damage_taken += opponent_attack_damage
        opponent_damage_taken += player_attack_damage

        if not opponent.is_alive():
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