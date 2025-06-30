import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press to enter to pick a card, or Q plus enter to quit: ").strip().upper()
    if user_input == "Q":
        #You quit the game
        break
    card_picked = random.choice(diamonds)
    diamonds.remove(card_picked)
    hand.append(card_picked)
    print(f"Your hand: {hand}")
    print(f"Remaining cards: {diamonds}\n")



if not diamonds:
    print("There are no more cards to pick.")