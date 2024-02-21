from players import *
from weapons import *
from arenas import * 
import random
import time

# Define a list of available weapons with their name and damage
def setup_weapons():
    return [
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

# Define a list of available arenas with their name and description
def setup_arenas():
    return [
        TheBattleArena("The Battle Arena", "A gladiatorial arena where heroes and villains clash."),
        TheForestArena("The Forest Arena", "A dense forest where fighters battle amidst trees and foliage."),
        TheDesertArena("The Desert Arena", "A scorching desert where combatants face off under the blazing sun."),
        TheIceArena("The Ice Arena", "A frozen wasteland where warriors duel on slippery ice.")
    ]

# Create available monsters with appropriate names
def setup_monsters():
    return [
        FierceWerewolf("Fierce Werewolf", 175, 45, howl_of_despair),
        MightyOrc("Mighty Orc", 160, 35, bloodlust),
        GiantOgre("Giant Ogre", 185, 50, berserker_strike),
        AncientDragon("Ancient Dragon", 200, 65, dragons_breath),
        CreepySkeleton("Creepy Skeleton", 150, 30, bone_shield),
        ScaryZombie("Scary Zombie", 155, 40, plague_swarm)
    ]

# Create a mapping of opponent classes to their special attacks
def setup_special_attacks():
    return {
        FierceWerewolf: howl_of_despair,
        MightyOrc: bloodlust,
        GiantOgre: berserker_strike,
        AncientDragon: dragons_breath,
        CreepySkeleton: bone_shield,
        ScaryZombie: plague_swarm
    }

def should_use_special_attack(player, opponent):
    # Example condition: use special attack randomly
    return random.choice([True, False])

def main():

    available_weapons = setup_weapons()
    available_arenas = setup_arenas()
    available_monsters = setup_monsters()
    special_attacks_mapping = setup_special_attacks()
    victories = 0
    player_choice = None  # Initialize to None or some default value

    # Modify the player choice section in the main function
    if player_choice == 'weapon':
        player_weapon = choose_weapon(available_weapons)
        player.weapon = player_weapon
        weapon_text = (f"You pick up the {player_weapon.name}.  Prepare for battle!")
        for char in weapon_text:
            print(char, end='', flush=True)
            time.sleep(0.08)

    # Introduction
    print()
    title_text = ("Welcome to the Arena Battler!")
    for char in title_text:
        print(char,end='',flush=True)
        time.sleep(0.04)
    print()

    # Create players
    time.sleep(0.5)
    player_name = input("Enter your character's name: ")
    player = Hero(player_name, 500, 45, rapid_assualt)
    print()
    arrival_text = (f"Our gladiator {player_name} arrives!  They will now choose an evermost terrifying arena to combat in.")
    for char in arrival_text:
        print(char, end='',flush=True)
        time.sleep(0.08)
    print()

    # List of all opponent classes
    opponent_classes = list(special_attacks_mapping.keys())

    # Present available arenas to choose
    available_arenas_text = ("Available Arenas:")
    for char in available_arenas_text:
        print(char, end='',flush=True)
        time.sleep(0.05)
    #print("Available Arenas:")
    for index, arena in enumerate(available_arenas, start=1):
        print(f"{index}. {arena.name}")
    print()
    # Get the Hero's choice
    choice = int(input("Choose an arena by entering its number: "))
    print()
    # Check if choice is valid
    if choice < 1 or choice > len(available_arenas):
        print("Invalid choice. Please choose a valid arena.")
        return

    # Select chosen arena
    chosen_arena = available_arenas[choice - 1]
    print()

    chosen_area_text = (f"""As {player.name} cautiously enters the dark, eerily silent room of {chosen_arena.name}, 
          a sense of foreboding fills the air. Suddenly, a faint noise catches your attention. You pause, 
          listening intently. The sound grows slightly louder, resembling a distant clattering. You inch 
          forward, your eyes scanning the dim surroundings. There, in the faint glow of light seeping 
          through an unseen source, lies a weapon, its metal gleaming with a promise of power. A moment 
          of decision arrives: Do you reach out to grasp the weapon, ready to face whatever lurks in the 
          shadows, or do you let fear take over and attempt to flee this ominous place?""") 
    for char in chosen_area_text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    if isinstance(chosen_arena, TheBattleArena):
        print()
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        print()
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            weapon_text2 = (f"You pick up the {player_weapon.name}.  Prepare for battle!")
            for char in weapon_text2:
                print(char, end='', flush=True)
                time.sleep(0.08)
        elif player_choice == 2:
            print()
            panic_text = ("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
            for char in panic_text:
                print(char,end='', flush=True)
                time.sleep(0.08)
            print()
            defeat_text = (f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}.  Better luck next time!")
            for char in defeat_text:
                print(char, end='', flush=True) 
                time.sleep(0.08)
            print()
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")

    # Additional narrative and player choices here
    elif isinstance(chosen_arena, TheForestArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print()
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
            print()
        elif player_choice == 2:
            print()
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
            print()
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            print()
            return  # Exit the function to end the game
        else:
            print("Invalid choice. Please choose a valid option.")
    elif isinstance(chosen_arena, TheDesertArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print()
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
            print()
        elif player_choice == 2:
            print()
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
            print()
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            print()
            return  # Exit the function to end the game
        else:
            print()
            print("Invalid choice. Please choose a valid option.")
            print()
    elif isinstance(chosen_arena, TheIceArena):
        print()
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        print()
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print()
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
            print()
        elif player_choice == 2:
            print()
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
            print()
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            print()
            return  # Exit the function to end the game
        else:
            print()
            print("Invalid choice. Please choose a valid option.")
            print()

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
    print()
    welcome_text = (f"Welcome, {player.name}!  You are in {chosen_arena.name}: {chosen_arena.description}")
    for char in welcome_text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    equip_text = (f"You are equipped with a {player.weapon.name}.")
    for char in equip_text:
        print(char, end='', flush=True)
        time.sleep(0.08)
    print()
    opponent_text = (f"Your opponent is {opponent.name}, entering the {chosen_arena.name}.")
    for char in opponent_text:
        print(char, end='', flush=True)
        time.sleep(0.08)
    print()

    # Simulate the interactive story based on the chosen arena
    if isinstance(chosen_arena, TheBattleArena):
        battle_arena_text = ("""As you step into the gladiatorial arena, a thunderous roar erupts from the sea of spectators, their 
        excitement palpable in the electric air. The atmosphere is charged with a mix of anticipation and tension, almost tangible 
        as the crowd's energy envelopes you. Each breath you take is heavy with the weight of expectation and the imminent challenge 
        that lies ahead. The ground beneath you vibrates with the collective clamor of the audience, a testament to the grand 
        spectacle that is about to unfold. You stand at the heart of the arena, ready to carve your fate in the sands of this 
        ancient battleground.""")
        for char in battle_arena_text:
            print(char, end='', flush=True)
            time.sleep(0.08)
        print()
        # Add more narrative specific to TheBattleArena
    elif isinstance(chosen_arena, TheForestArena):
        print("""You find yourself in the depths of a dense forest, surrounded by the imposing heights of towering trees reaching 
        skyward. The atmosphere is thick with the rustling whispers of leaves and the enigmatic symphony of the forest's hidden 
        dwellers. Echoes of distant bird calls and the soft crunch of underbrush under the feet of unseen creatures fill the air 
        with a sense of mystery. The scent of the forest envelops you, a rich blend of damp earth, vibrant greenery, and the faint 
        fragrance of wildflowers hidden in the shadows. Shafts of light filter through the dense canopy, creating a play of light 
        and shadow that weaves a tapestry of intrigue and wonder, inviting you deeper into the forest's alluring mystery.""")
        print()
        # Add more narrative specific to TheForestArena
    elif isinstance(chosen_arena, TheDesertArena):
        print("""The relentless sun blazes overhead in the vast desert, casting its scorching rays upon the endless sea of sand. 
        The heat is oppressive, almost suffocating, as it envelopes everything under the wide, azure sky. As you gaze out, the 
        sand forms an unbroken horizon, merging with the heat haze in the distance, creating an illusion of infinity.""")
        print()
        # Add more narrative specific to TheDesertArena
    elif isinstance(chosen_arena, TheIceArena):
        print("""You find yourself in the midst of a vast, frozen expanse, where the ground is a solid sheet of ice under your feet.
        The air is piercingly cold, sending shivers down your spine. In the eerie silence of this frigid landscape, the occasional 
        sound of ice fracturing and shifting resonates, echoing hauntingly in the distance.""")
        print()
        # Add more narrative specific to TheIceArena

    # Initialize winning_weapon outside the battle loop
    winning_weapon = None

    # Initialize damage counters
    player_damage_taken = 0
    opponent_damage_taken = 0

    # Simulate a battle
    while player.is_alive() and opponent.is_alive():
        # Initialize attack damages for this turn
        player_attack_damage = 0
        opponent_attack_damage = 0

        # Player's turn
        if should_use_special_attack(player, opponent):
            player_attack_damage = player.special_attack(opponent)
            print()
            special_attack_text = (f"{player.name} used a special attack on {opponent.name}, dealing {player_attack_damage} damage!")
            for char in special_attack_text:
                print(char,end='',flush=True)
                time.sleep(0.08)
            print()
        else:
            # Regular attack
            player_attack_damage = player.attack(opponent)
            print()
            print(f"{player.name} attacked {opponent.name}, dealing {player_attack_damage} damage!")
            print()

        # Opponent's turn
        if opponent.is_alive():
            if should_use_special_attack(opponent, player):
                opponent_attack_damage = opponent.special_attack(player)
                print()
                print(f"{opponent.name} used a special attack on {player.name}, dealing {opponent_attack_damage} damage!")
                print()
            else:
                opponent_attack_damage = opponent.attack(player)
                print()
                print(f"{opponent.name} attacked {player.name}, dealing {opponent_attack_damage} damage!")
                print()

        # Track damage taken by both player and opponent
        player_damage_taken += opponent_attack_damage
        opponent_damage_taken += player_attack_damage

        # Check the outcome of the battle
        if not opponent.is_alive():
            winning_weapon = player.weapon.name
            print()
            print(f"Congratulations, {player.name}! You emerged victorious with {winning_weapon}.")
            print()
            victories += 1
        elif not player.is_alive():
            print()
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            print()
            return  # Exit the function to end the game

    # Display damage information
    print()
    print(f"Total damage dealt to {player.name}: {player_damage_taken}")
    print()
    print(f"Total damage dealt to {opponent.name}: {opponent_damage_taken}")
    print()

    # Present available arenas to choose
    print("You trudge forward completing the arena...")
    print()
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

    print(f"""As {player.name} cautiously enters the dark, eerily silent room of {chosen_arena.name}, 
          a sense of foreboding fills the air. Suddenly, a faint noise catches your attention. You pause, 
          listening intently. The sound grows slightly louder, resembling a distant clattering. You inch 
          forward, your eyes scanning the dim surroundings. There, in the faint glow of light seeping 
          through an unseen source, lies a weapon, its metal gleaming with a promise of power. A moment 
          of decision arrives: Do you reach out to grasp the weapon, ready to face whatever lurks in the 
          shadows, or do you let fear take over and attempt to flee this ominous place?""")

    if isinstance(chosen_arena, TheBattleArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print()
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
            print()
            print(f"Unfortunately, {player.name} has been defeated in {chosen_arena.name}. Better luck next time!")
            print()
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
        print("""As you step into the gladiatorial arena, a thunderous roar erupts from the sea of spectators, their 
        excitement palpable in the electric air. The atmosphere is charged with a mix of anticipation and tension, almost tangible 
        as the crowd's energy envelopes you. Each breath you take is heavy with the weight of expectation and the imminent challenge 
        that lies ahead. The ground beneath you vibrates with the collective clamor of the audience, a testament to the grand 
        spectacle that is about to unfold. You stand at the heart of the arena, ready to carve your fate in the sands of this 
        ancient battleground.""")
        # Add more narrative specific to TheBattleArena
    elif isinstance(chosen_arena, TheForestArena):
        print("""You find yourself in the depths of a dense forest, surrounded by the imposing heights of towering trees reaching 
        skyward. The atmosphere is thick with the rustling whispers of leaves and the enigmatic symphony of the forest's hidden 
        dwellers. Echoes of distant bird calls and the soft crunch of underbrush under the feet of unseen creatures fill the air 
        with a sense of mystery. The scent of the forest envelops you, a rich blend of damp earth, vibrant greenery, and the faint 
        fragrance of wildflowers hidden in the shadows. Shafts of light filter through the dense canopy, creating a play of light 
        and shadow that weaves a tapestry of intrigue and wonder, inviting you deeper into the forest's alluring mystery.""")
        # Add more narrative specific to TheForestArena
    elif isinstance(chosen_arena, TheDesertArena):
        print("""The relentless sun blazes overhead in the vast desert, casting its scorching rays upon the endless sea of sand. 
        The heat is oppressive, almost suffocating, as it envelopes everything under the wide, azure sky. As you gaze out, the 
        sand forms an unbroken horizon, merging with the heat haze in the distance, creating an illusion of infinity.""")
        # Add more narrative specific to TheDesertArena
    elif isinstance(chosen_arena, TheIceArena):
        print("""You find yourself in the midst of a vast, frozen expanse, where the ground is a solid sheet of ice under your feet.
        The air is piercingly cold, sending shivers down your spine. In the eerie silence of this frigid landscape, the occasional 
        sound of ice fracturing and shifting resonates, echoing hauntingly in the distance.""")
        # Add more narrative specific to TheIceArena

    # Initialize winning_weapon outside the battle loop
    winning_weapon = None

    # Initialize damage counters
    player_damage_taken = 0
    opponent_damage_taken = 0

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

    print(f"""As {player.name} cautiously enters the dark, eerily silent room of {chosen_arena.name}, 
          a sense of foreboding fills the air. Suddenly, a faint noise catches your attention. You pause, 
          listening intently. The sound grows slightly louder, resembling a distant clattering. You inch 
          forward, your eyes scanning the dim surroundings. There, in the faint glow of light seeping 
          through an unseen source, lies a weapon, its metal gleaming with a promise of power. A moment 
          of decision arrives: Do you reach out to grasp the weapon, ready to face whatever lurks in the 
          shadows, or do you let fear take over and attempt to flee this ominous place?""")

    if isinstance(chosen_arena, TheBattleArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
        print("""As you step into the gladiatorial arena, a thunderous roar erupts from the sea of spectators, their 
        excitement palpable in the electric air. The atmosphere is charged with a mix of anticipation and tension, almost tangible 
        as the crowd's energy envelopes you. Each breath you take is heavy with the weight of expectation and the imminent challenge 
        that lies ahead. The ground beneath you vibrates with the collective clamor of the audience, a testament to the grand 
        spectacle that is about to unfold. You stand at the heart of the arena, ready to carve your fate in the sands of this 
        ancient battleground.""")
        # Add more narrative specific to TheBattleArena
    elif isinstance(chosen_arena, TheForestArena):
        print("""You find yourself in the depths of a dense forest, surrounded by the imposing heights of towering trees reaching 
        skyward. The atmosphere is thick with the rustling whispers of leaves and the enigmatic symphony of the forest's hidden 
        dwellers. Echoes of distant bird calls and the soft crunch of underbrush under the feet of unseen creatures fill the air 
        with a sense of mystery. The scent of the forest envelops you, a rich blend of damp earth, vibrant greenery, and the faint 
        fragrance of wildflowers hidden in the shadows. Shafts of light filter through the dense canopy, creating a play of light 
        and shadow that weaves a tapestry of intrigue and wonder, inviting you deeper into the forest's alluring mystery.""")
        # Add more narrative specific to TheForestArena
    elif isinstance(chosen_arena, TheDesertArena):
        print("""The relentless sun blazes overhead in the vast desert, casting its scorching rays upon the endless sea of sand. 
        The heat is oppressive, almost suffocating, as it envelopes everything under the wide, azure sky. As you gaze out, the 
        sand forms an unbroken horizon, merging with the heat haze in the distance, creating an illusion of infinity.""")
        # Add more narrative specific to TheDesertArena
    elif isinstance(chosen_arena, TheIceArena):
        print("""You find yourself in the midst of a vast, frozen expanse, where the ground is a solid sheet of ice under your feet.
        The air is piercingly cold, sending shivers down your spine. In the eerie silence of this frigid landscape, the occasional 
        sound of ice fracturing and shifting resonates, echoing hauntingly in the distance.""")
        # Add more narrative specific to TheIceArena

    # Initialize winning_weapon outside the battle loop
    winning_weapon = None

    # Initialize damage counters
    player_damage_taken = 0
    opponent_damage_taken = 0

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

    print(f"""As {player.name} cautiously enters the dark, eerily silent room of {chosen_arena.name}, 
          a sense of foreboding fills the air. Suddenly, a faint noise catches your attention. You pause, 
          listening intently. The sound grows slightly louder, resembling a distant clattering. You inch 
          forward, your eyes scanning the dim surroundings. There, in the faint glow of light seeping 
          through an unseen source, lies a weapon, its metal gleaming with a promise of power. A moment 
          of decision arrives: Do you reach out to grasp the weapon, ready to face whatever lurks in the 
          shadows, or do you let fear take over and attempt to flee this ominous place?""")

    if isinstance(chosen_arena, TheBattleArena):
        player_choice = int(input("Choose an option: 1 for weapon, 2 to run: "))
        if player_choice == 1:
            player_weapon = choose_weapon(available_weapons)
            player.weapon = player_weapon
            print(f"You pick up the {player_weapon.name}. Prepare for battle!")
        elif player_choice == 2:
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
            print("""In a sudden surge of panic, you attempt a desperate escape. But alas, your path is blocked, 
            leaving you trapped and vulnerable. With no way out, you face an inevitable defeat, overwhelmed by 
            the circumstances that have cunningly cornered you.""")
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
        print("""As you step into the gladiatorial arena, a thunderous roar erupts from the sea of spectators, their 
        excitement palpable in the electric air. The atmosphere is charged with a mix of anticipation and tension, almost tangible 
        as the crowd's energy envelopes you. Each breath you take is heavy with the weight of expectation and the imminent challenge 
        that lies ahead. The ground beneath you vibrates with the collective clamor of the audience, a testament to the grand 
        spectacle that is about to unfold. You stand at the heart of the arena, ready to carve your fate in the sands of this 
        ancient battleground.""")
        # Add more narrative specific to TheBattleArena
    elif isinstance(chosen_arena, TheForestArena):
        print("""You find yourself in the depths of a dense forest, surrounded by the imposing heights of towering trees reaching 
        skyward. The atmosphere is thick with the rustling whispers of leaves and the enigmatic symphony of the forest's hidden 
        dwellers. Echoes of distant bird calls and the soft crunch of underbrush under the feet of unseen creatures fill the air 
        with a sense of mystery. The scent of the forest envelops you, a rich blend of damp earth, vibrant greenery, and the faint 
        fragrance of wildflowers hidden in the shadows. Shafts of light filter through the dense canopy, creating a play of light 
        and shadow that weaves a tapestry of intrigue and wonder, inviting you deeper into the forest's alluring mystery.""")
        # Add more narrative specific to TheForestArena
    elif isinstance(chosen_arena, TheDesertArena):
        print("""The relentless sun blazes overhead in the vast desert, casting its scorching rays upon the endless sea of sand. 
        The heat is oppressive, almost suffocating, as it envelopes everything under the wide, azure sky. As you gaze out, the 
        sand forms an unbroken horizon, merging with the heat haze in the distance, creating an illusion of infinity.""")
        # Add more narrative specific to TheDesertArena
    elif isinstance(chosen_arena, TheIceArena):
        print("""You find yourself in the midst of a vast, frozen expanse, where the ground is a solid sheet of ice under your feet.
        The air is piercingly cold, sending shivers down your spine. In the eerie silence of this frigid landscape, the occasional 
        sound of ice fracturing and shifting resonates, echoing hauntingly in the distance.""")
        # Add more narrative specific to TheIceArena

    # Initialize winning_weapon outside the battle loop
    winning_weapon = None

    # Initialize damage counters
    player_damage_taken = 0
    opponent_damage_taken = 0

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

    if victories == len(available_arenas):

        victory_text = (f"""Behold the spectacular triumph! The invincible {player.name} has achieved a feat beyond imagination,
        reigning victorious in every arena known to the realms. Their prowess and skill have marked them as the 
        unparalleled Champion of the Realms, a title resonating with unmatched honor and strength. In the chronicles of 
        time, their name will be revered as a symbol of ultimate mastery and heroic spirit. Across every land and kingdom, 
        their extraordinary achievement is celebrated, heralding an era of awe inspired by their unmatched excellence!""")
        for char in victory_text:
            print(char,end='', flush=True)
            time.sleep(0.08)

if __name__ == "__main__":
    main()