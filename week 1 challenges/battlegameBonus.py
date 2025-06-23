"""
Mathias Adikpon 
Battle game (Bonus)
Jun 21, 2025
"""

def start_game():
    # Declare variables for characters
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    dwarf = "Dwarf"

    # Assign hp to characters
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    dwarf_hp = 120

    # Assign damage to characters
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    dwarf_damage = 80

    # Assign hp and damage to the Dragon
    dragon_hp = 300
    dragon_damage = 50

    # Choose a character (Player Choice)
    while True:
        # Show the player a list of options to choose from
        print("1)\t Wizard")
        print("2)\t Elf")
        print("3)\t Human")
        print("4)\t Dwarf")

        # Prompt the user to choose a character
        character = input("Choose your character: ").strip().lower()

        if character in ["wizard", "1"]:
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character in ["elf", "2"]:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character in ["human", "3"]:
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if character in ["dwarf", "4"]:
            character = dwarf
            my_hp = dwarf_hp
            my_damage = dwarf_damage
            break

        print("Unknown character")

    print("You have chosen the character:", character)
    print("Health ", my_hp)
    print("Damage ", my_damage)

    # Task 4: Battle with the Dragon!
    while True:
        dragon_hp = dragon_hp - my_damage
        print("\nThe", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon_hp)
        if dragon_hp <= 0:
            print("\nThe Dragon has lost the battle")
            break

        my_hp = my_hp - dragon_damage
        print("\nThe Dragon strikes back at", character)
        print("The", character + "'s","hitpoints are now:", my_hp) 
        if my_hp <= 0:
            print("\nThe ", character, "has lost the battle.")
            break

def game_question():
    while True:
        answer = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if answer in ["yes", "y", "sure", "ok", "yeah", "yep"]:
            start_game()
           
        elif answer in ["no", "n"]:
            print("Thank you for playing!")
            break
        else:
            print("Please answer with 'yes' or 'no'.")

if __name__ == "__main__":
    print("\nWelcome to the Battle Game!")
    game_question()
    print("Game Over")