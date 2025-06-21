# Task 1:  Set Up the Game

#3) 4) Declare three variables with the following names: wizard, elf, human

wizard = "Wizard"
elf = "Elf"
human = "Human"

"""
5) Declare three variables, set to Integer values that indicate the hp of each character.
The hp of a wizard is 70
The hp of an elf is 100
The hp of a human is 150
Example: wizard_hp = 70
"""
wizard_hp = 70
elf_hp = 100
human_hp = 150

"""
6) Declare three more variables having Integer values that indicate the damage of each character.
The damage of a Wizard is 150
The damage of an Elf is 100
The damage of a Human is 20
Example: wizard_damage = 150
"""
wizard_damage = 150
elf_damage = 100
human_damage = 20

"""
7) Also declare two variables that set the hp and damage for the Dragon - 300 hp and 50 damage.
Example: dragon_hp = 300
"""
dragon_hp = 300
dragon_damage = 50




# Task 3: Player Choice
"""
Wrap all the code you created in Task 2 in an infinite while loop that uses the True condition.

"""
while True:
    # Task 2: Prompt Player
    # 1. Show the player a list of options to choose from, using the print() function.
    print("1)\t Wizard")
    print("2)\t Elf")
    print("3)\t Human")

    """
    2. Use the input() function to prompt the user with the String: "Choose your character: 
    3. Assign the value returned from the input function to a variable named character.
    """
    character = input("Choose your character: ")

    """
    
    2.Inside the while loop, write a sequence of three if statements to handle the three options.
    """
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print("Unknown character")

print("You have chosen the character:", character)
print("Health ", my_hp)
print("Damage ", my_damage)