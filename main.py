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
    # player = Player(player_name, 100, 20, "Rapid Assault: The player performs a rapid succession of strikes against a single target or multiple nearby enemies, dealing significant damage.")

    available_monsters = [
        # Werewolf(player_name, 75, 45, "Howl of Despair: The werewolf lets out a terrifying howl that can debuff enemies within a certain radius, reducing their attack power or causing fear, which might make them miss their next attack."),
        Werewolf(player_name, 75, 45, howl_of_despair),
        # Orc(player_name, 60, 35, "Bloodlust: With each hit that successfully damages an opponent, the orc gains a small amount of health or a temporary increase in attack power, representing its battle-fueled frenzy."),
        Orc(player_name, 60, 35, bloodlust),
        # Ogre(player_name, 85, 50, "Berserker Strike: The ogre unleashes a series of powerful blows, each hit dealing increased damage. This could involve swinging a massive weapon or using brute force to pummel the enemy."),
        Ogre(player_name, 85, 50, berserker_strike),
        # Dragon(player_name, 200, 65, "Dragon's Breath: The dragon unleashes its ancient, elemental power in a devastating breath attack that not only causes direct damage but also alters the battlefield in a significant way."),
        Dragon(player_name, 200, 65, dragons_breath),
        # Skeleton(player_name, 50, 30, "Bone Shield: As the bones fly out, some of them circle back to form a temporary shield around the skeleton, providing a defensive buff or absorbing a certain amount of damage from incoming attacks."),
        Skeleton(player_name, 50, 30, bone_shield),
        # Zombie(player_name, 55, 40, "Plague Swarm: The zombie unleashes a virulent, contagious plague that not only damages but also has a chance to infect enemies, potentially turning them into weaker zombie minions.")
        Zombie(player_name, 55, 40, plague_swarm)
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
    # Decide whether to use a special attack
        if should_use_special_attack(player, opponent):
            special_attack_damage = player.special_attack(opponent)
            print(f"{player.name} used a special attack on {opponent.name} dealing {special_attack_damage} damage!")

        # Continue with regular attacks
        player_attack_damage = player.attack(opponent)
        print(f"{player.name} dealt {player_attack_damage} damage to {opponent.name}!")

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