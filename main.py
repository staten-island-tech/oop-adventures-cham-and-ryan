from location import Location
from random import randint
x = 0
forest = Location("Forest", ["Wood, 80% Rarity, Worth 1 Gold Coin", "Pre-Historic Human 15% Chance", 
                             "Bear Head 5% Rarity 50 Gold Coins", "Jarvis' left pinky toenail 0.01% Rarity, 1000 Gold Coins"])
forest.information()

cave = Location("Cave", ["Dog Feces, 50% Rarity, Worth 0 Gold Coins",
                         "Special Miner's hat, 30% Worth, 15 Coins",
                         "Even more Special Miner's hat, 10% Rarity, 30 Coins",
                         "Iron, 6% Rarity, Worth 50 Gold","Diamonds, 4% Rarity, Worth 150 Gold", 
                         "Mr. Whalen, 0.02% Rarity, 0.01% Chance of 1000 Coin gain"])
cave.information()
question = input("do you want to go to a forest or cave?")

def forest(y):
    i = randint(1, 10000)
    if i <= 8000:
        print("thats a lot of wood sir")
        y += 1
        return y
    elif i > 8000 and i <= 9500:
        print("you got brutally stabbed to death and died while looking at your heart on the ground")
    elif i > 9500 and i <= 9999:
        print("is that a bear head i see so sigma")
    else:
        print("woah sir thats a nice toenail, i bet it's jarvis'")

def cave():
    i = randint(1, 10000)
    if i <= 5000:
        print("wow, you found dog feces. you gained 0 gold")
    elif i > 5000 and i <= 8000:
        print("Wow, you found special miner's hat, you gained 15 coins")
    elif i > 8000 and i <= 9000:
        print("Wow, you found the even more special miner's hat")
    elif i > 9000 and i <= 9600:
        print("Iron!!, wow it's prettier than you")
    elif i > 9600 and i <= 9998:
        print("DIAMONDS, wow ur so rich")
    elif i == 9999:
        print("mr whalen??, you died to heart attack after he lowered your HOS")
    else:
        print("mr whalen??, he highers your HOS and you gain 1000 coins")

if question == "forest":
    x = forest(x)
elif question == "cave":
    cave()

print(f"You have {x} gold coins.")