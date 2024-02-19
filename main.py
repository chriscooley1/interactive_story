from players import *
from weapons import *
from arenas import *
import random

def main():

    player_choice = None  # Initialize to None or some default value
    victories = 0
    
    # Define a list of available weapons with their name and damage
    available_weapons = [
        Sword("Sword", 30),
        Axe("Axe", 35),
        Bow("Bow", 25),
        Dagger("Dagger", 20),
        Mace("Mace", 40)
    ]

    # Add this function to allow the player to choose a weapon
    def choose_weapon(available_weapons):
        print("Available Weapons:")
        for index, weapon in enumerate(available_weapons, start=1):
            print(f"{index}. {weapon.name} (Damage: {weapon.damage})")
        choice = int(input("Choose a weapon by entering its number: "))
        if 1 <= choice <= len(available_weapons):
            return available_weapons[choice - 1]
        else:
            print("Invalid choice. Defaulting to the first weapon.")
            return available_weapons[0]

    # Modify the player choice section in the main function
    if player_choice == 'weapon':
        player_weapon = choose_weapon(available_weapons)
        player.weapon = player_weapon
        print(f"You pick up the {player_weapon.name}. Prepare for battle!")

    # Define a list of available arenas with their name and description
    available_arenas = [
        TheBattleArena("The Battle Arena", "A gladiatorial arena where heroes and villains clash."),
        TheForestArena("The Forest Arena", "A dense forest where fighters battle amidst trees and foliage."),
        TheDesertArena("The Desert Arena", "A scorching desert where combatants face off under the blazing sun."),
        TheIceArena("The Ice Arena", "A frozen wasteland where warriors duel on slippery ice.")
    ]

    # Create players
    player_name = input("Enter your character's name: ")
    player = Hero(player_name, 500, 45, rapid_assualt)

    # Create available monsters with appropriate names
    available_monsters = [
        FierceWerewolf("Fierce Werewolf", 175, 45, howl_of_despair),
        MightyOrc("Mighty Orc", 160, 35, bloodlust),
        GiantOgre("Giant Ogre", 185, 50, berserker_strike),
        AncientDragon("Ancient Dragon", 200, 65, dragons_breath),
        CreepySkeleton("Creepy Skeleton", 150, 30, bone_shield),
        ScaryZombie("Scary Zombie", 155, 40, plague_swarm)
    ]

    # Create a mapping of opponent classes to their special attacks
    special_attacks_mapping = {
        FierceWerewolf: howl_of_despair,
        MightyOrc: bloodlust,
        GiantOgre: berserker_strike,
        AncientDragon: dragons_breath,
        CreepySkeleton: bone_shield,
        ScaryZombie: plague_swarm
    }

    # List of all opponent classes
    opponent_classes = list(special_attacks_mapping.keys())

    # Present available arenas to choose
    print("Available Arenas:")
    for index, arena in enumerate(available_arenas, start=1):
        print(f"{index}. {arena.name}")

    # Get the Hero's choice
    choice = int(input("Choose an arena by entering its number: "))

    # Check if choice is valid
    if choice < 1 or choice > len(available_arenas):
        print("Invalid choice. Please choose a valid arena.")
        return

    # Select chosen arena
    chosen_arena = available_arenas[choice - 1]

    if isinstance(chosen_arena, TheBattleArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")

    # Additional narrative and player choices here
    elif isinstance(chosen_arena, TheForestArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheDesertArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheIceArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")

    # Reset player's health and status for each new battle
    player.health = 100

    # Create an opponent
    if random.choice([True, False]):
        opponent = random.choice(available_monsters)
    else:
        opponent_class = random.choice(opponent_classes)
        opponent_special_attack = special_attacks_mapping[opponent_class]
        opponent_name = f"{opponent_class.__name__}"
        opponent = opponent_class(opponent_name, 100, 20, opponent_special_attack)

    # Add players to the chosen arena
    chosen_arena.add_player(player)
    chosen_arena.add_player(opponent)

    # Announcement of the arena, weapon, and opponent
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player.weapon.name}.")
    print(f"Your opponent is {opponent.name}, entering the {chosen_arena.name}.")

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

        # Opponent's turn
        if opponent.is_alive():
            if should_use_special_attack(opponent, player):
                opponent_attack_damage = opponent.special_attack(player)
                print(f"{opponent.name} used a special attack on {player.name}, dealing {opponent_attack_damage} damage!")
            else:
                opponent_attack_damage = opponent.attack(player)
                print(f"{opponent.name} attacked {player.name}, dealing {opponent_attack_damage} damage!")

        # Track damage taken by both player and opponent
        player_damage_taken += opponent_attack_damage
        opponent_damage_taken += player_attack_damage

        # Check the outcome of the battle
        if not opponent.is_alive():
            winning_weapon = player.weapon.name
            print(f"Congratulations, {player.name}! You emerged victorious with {winning_weapon}.")
            victories += 1
        elif not player.is_alive():
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game

    # Display damage information
    print(f"Total damage dealt to {player.name}: {player_damage_taken}")
    print(f"Total damage dealt to {opponent.name}: {opponent_damage_taken}")

    # Present available arenas to choose
    print("Available Arenas:")
    for index, arena in enumerate(available_arenas, start=1):
        print(f"{index}. {arena.name}")

    # Get the Hero's choice
    choice = int(input("Choose an arena by entering its number: "))

    # Check if choice is valid
    if choice < 1 or choice > len(available_arenas):
        print("Invalid choice. Please choose a valid arena.")
        return

    # Select chosen arena
    chosen_arena = available_arenas[choice - 1]

    if isinstance(chosen_arena, TheBattleArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    # Additional narrative and player choices here
    elif isinstance(chosen_arena, TheForestArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheDesertArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheIceArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")

    # Reset player's health and status for each new battle
    player.health = 100

    # Create an opponent
    if random.choice([True, False]):
        opponent = random.choice(available_monsters)
    else:
        opponent_class = random.choice(opponent_classes)
        opponent_special_attack = special_attacks_mapping[opponent_class]
        opponent_name = f"{opponent_class.__name__}"
        opponent = opponent_class(opponent_name, 100, 20, opponent_special_attack)

    # Add players to the chosen arena
    chosen_arena.add_player(player)
    chosen_arena.add_player(opponent)

    # Announce the arena and battle
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player_weapon.name}.")
    print(f"Your opponent is {opponent.name}, entering the {chosen_arena.name}.")

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

        # Opponent's turn
        if opponent.is_alive():
            if should_use_special_attack(opponent, player):
                opponent_attack_damage = opponent.special_attack(player)
                print(f"{opponent.name} used a special attack on {player.name}, dealing {opponent_attack_damage} damage!")
            else:
                opponent_attack_damage = opponent.attack(player)
                print(f"{opponent.name} attacked {player.name}, dealing {opponent_attack_damage} damage!")

        # Track damage taken by both player and opponent
        player_damage_taken += opponent_attack_damage
        opponent_damage_taken += player_attack_damage

        # Check the outcome of the battle
        if not opponent.is_alive():
            winning_weapon = player.weapon.name
            print(f"Congratulations, {player.name}! You emerged victorious with {winning_weapon}.")
            victories += 1
        elif not player.is_alive():
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
    
    # Display damage information
    print(f"Total damage dealt to {player.name}: {player_damage_taken}")
    print(f"Total damage dealt to {opponent.name}: {opponent_damage_taken}")

    # Check if player won the battle
    if player.is_alive():
        print(f"Congratulations, {player.name}! You emerged victorious in {chosen_arena.name}.")
    else:
        print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
        return  # Exit the function to end the game

    # Present available arenas to choose
    print("Available Arenas:")
    for index, arena in enumerate(available_arenas, start=1):
        print(f"{index}. {arena.name}")

    # Get the Hero's choice
    choice = int(input("Choose an arena by entering its number: "))

    # Check if choice is valid
    if choice < 1 or choice > len(available_arenas):
        print("Invalid choice. Please choose a valid arena.")
        return

    # Select chosen arena
    chosen_arena = available_arenas[choice - 1]

    if isinstance(chosen_arena, TheBattleArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    # Additional narrative and player choices here
    elif isinstance(chosen_arena, TheForestArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheDesertArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheIceArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")

    # Reset player's health and status for each new battle
    player.health = 100

    # Create an opponent
    if random.choice([True, False]):
        opponent = random.choice(available_monsters)
    else:
        opponent_class = random.choice(opponent_classes)
        opponent_special_attack = special_attacks_mapping[opponent_class]
        opponent_name = f"{opponent_class.__name__}"
        opponent = opponent_class(opponent_name, 100, 20, opponent_special_attack)

    # Add players to the chosen arena
    chosen_arena.add_player(player)
    chosen_arena.add_player(opponent)

    # Announce the arena and battle
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player_weapon.name}.")
    print(f"Your opponent is {opponent.name}, entering the {chosen_arena.name}.")

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

        # Opponent's turn
        if opponent.is_alive():
            if should_use_special_attack(opponent, player):
                opponent_attack_damage = opponent.special_attack(player)
                print(f"{opponent.name} used a special attack on {player.name}, dealing {opponent_attack_damage} damage!")
            else:
                opponent_attack_damage = opponent.attack(player)
                print(f"{opponent.name} attacked {player.name}, dealing {opponent_attack_damage} damage!")

        # Track damage taken by both player and opponent
        player_damage_taken += opponent_attack_damage
        opponent_damage_taken += player_attack_damage

        # Check the outcome of the battle
        if not opponent.is_alive():
            winning_weapon = player.weapon.name
            print(f"Congratulations, {player.name}! You emerged victorious with {winning_weapon}.")
            victories += 1
        elif not player.is_alive():
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game

    # Present available arenas to choose
    print("Available Arenas:")
    for index, arena in enumerate(available_arenas, start=1):
        print(f"{index}. {arena.name}")

    # Get the Hero's choice
    choice = int(input("Choose an arena by entering its number: "))

    # Check if choice is valid
    if choice < 1 or choice > len(available_arenas):
        print("Invalid choice. Please choose a valid arena.")
        return

    # Select chosen arena
    chosen_arena = available_arenas[choice - 1]

    if isinstance(chosen_arena, TheBattleArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    # Additional narrative and player choices here
    elif isinstance(chosen_arena, TheForestArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheDesertArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheIceArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("You panic and try to run away. Unfortunately, you are cornered and defeated.")
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")

    # Reset player's health and status for each new battle
    player.health = 100

    # Create an opponent
    if random.choice([True, False]):
        opponent = random.choice(available_monsters)
    else:
        opponent_class = random.choice(opponent_classes)
        opponent_special_attack = special_attacks_mapping[opponent_class]
        opponent_name = f"{opponent_class.__name__}"
        opponent = opponent_class(opponent_name, 100, 20, opponent_special_attack)

    # Add players to the chosen arena
    chosen_arena.add_player(player)
    chosen_arena.add_player(opponent)

    # Announce the arena and battle
    print(f"Welcome, {player.name}! You are in {chosen_arena.name}: {chosen_arena.description}")
    print(f"You are equipped with a {player_weapon.name}.")
    print(f"Your opponent is {opponent.name}, entering the {chosen_arena.name}.")

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

        # Opponent's turn
        if opponent.is_alive():
            if should_use_special_attack(opponent, player):
                opponent_attack_damage = opponent.special_attack(player)
                print(f"{opponent.name} used a special attack on {player.name}, dealing {opponent_attack_damage} damage!")
            else:
                opponent_attack_damage = opponent.attack(player)
                print(f"{opponent.name} attacked {player.name}, dealing {opponent_attack_damage} damage!")

        # Track damage taken by both player and opponent
        player_damage_taken += opponent_attack_damage
        opponent_damage_taken += player_attack_damage

        # Check the outcome of the battle
        if not opponent.is_alive():
            winning_weapon = player.weapon.name
            print(f"Congratulations, {player.name}! You emerged victorious with {winning_weapon}.")
            victories += 1
        elif not player.is_alive():
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            return  # Exit the function to end the game

    # Display damage information
    print(f"Total damage dealt to {player.name}: {player_damage_taken}")
    print(f"Total damage dealt to {opponent.name}: {opponent_damage_taken}")

    # Check if player won the battle
    if player.is_alive():
        print(f"Congratulations, {player.name}! You emerged victorious in {chosen_arena.name}.")
    else:
        print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
        return  # Exit the function to end the game
    if victories == len(available_arenas):
        print(f"Amazing! {player.name} has emerged victorious in all arenas! A true champion of the realms!")

if __name__ == "__main__":
    main()