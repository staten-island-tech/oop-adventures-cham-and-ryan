from location import Location
from random import randint
import time, os, json

x = 0

with open("coins.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    x = json.load(f)[0]


axe = False
flashlight = False
metaldetector = False
shovel = False
pickaxe = False

Equip = input("What item do you want to use?(the ones you have dont lie):")

if Equip == "axe":
    axe = True
elif Equip == "flashlight":
    flashlight = True
elif Equip == "metaldetector":
    metaldetector = True
    if metaldetector == True:
        print("Metaldetector:True")
elif Equip == "shovel":
    shovel = True
elif Equip == "pickaxe":
    pickaxe = True
elif Equip == "None":
    axe = False
    flashlight = False
    metaldetector = False
    shovel = False
    pickaxe = False




forest = Location("Forest", [
    "Wood, 80% Rarity", 
    "Worth 1 Gold Coin", 
    "Pre-Historic Human 20% Chance", 
    "Bear Head 20% Rarity 50 Gold Coins", 
    "Jarvis left pinky toenail 0.01% Rarity",
    "1000 Gold Coins"
    ])

# forest.information()

cave = Location("Cave", ["Dog Feces, 20% Rarity, Worth 0 Coins",
                         "Vbucks, 30% Rarity, Worth 5 Coins"
                         "Special Miner's hat, 30% Rarity, 15 Coins",
                         "Even more Special Miner's hat, 20% Rarity, 30 Coins",
                         "Iron, 6% Rarity, Worth 50 Gold","Diamonds, 4% Rarity, Worth 150 Gold", 
                         "Mr. Whalen, 0.02% Rarity, 0.01% Chance of 1000 Coin gain"])

dungeon = Location("Dungeon", ["Guard, 20% Rarity, You Die",
                               "Spike, 20% Rarity, You Die.",
                               "Fake Stash of Diamonds(It was bombs), 10% Rarity, You Die.",
                               "Real Stash of Diamonds, 10% Rarity, Worth 1000 Gold",
                               "Mr. Whalen's password (You can give yourself HOS Points),5% Rarity, Worth 1200 Gold",
                               "Vault of Gold, 30% Rarity, Worth 800 Gold",
                               "Ms. Zerega's Homework pass, 5% Rarity, Worth 2000 Gold"])

# << Function With Butter >> #

# cave.information()
#def print(text, speedo):
    #for char in text:
        #print(char, end="")
        #time.sleep(speedo)

def forest(y):
    i = randint(1, 10000)

    if i <= 5000:

        print("Wow you have a lot of wood, I'll give you 1 gold coin for them", )

        y += 1

        print(f"You have {y} gold coins.")

        ryan = input('again?')

        if ryan == "yes":
            return forest(y)

        return y
    
    elif i > 5000 and i <= 7000:
        print("you got brutally stabbed to death and died while looking at your heart on the ground")
        
        return 0
    
    elif i > 7000 and i <= 9999:
        print("is that a bear head i see so sigma")
        y += 35
        print(f"You have {y} gold coins.")
        ryan = input('again?')

        if ryan == "yes":
            return forest(y)

        return y
    
    else:
        print("woah sir thats a nice toenail, i bet it's jarvis'")
        y += 1000
        print(f"You have {y} gold coins.")
        ryan = input('again?')

        if ryan == "yes":
            return forest(y)

        return y

def cave(z):

    i = randint(1, 10000)
    if metaldetector:
        i = randint (1, 20000)
    if shovel:
        i = randint (1, 10000)
    if ((not shovel) and i < 2000) or (shovel and i < 1000):
        print("wow, you found dog feces. you gained 0 coins")
        z += 0
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i >= 2000 and i < 5000:
        print("VBUCKS!!, you gained 5 Gold Coins")
        z += 5
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i > 5000 and i <= 6000:
        print("Wow, you found special miner's hat, you gained 15 coins")
        z += 15
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i>6000 and i <= 7000:
        print("You unfortunately died to rock collapse")
        
        return 0
    elif i > 7000 and i <= 9000:
        print("Wow, you found the even more special miner's hat, you gained 30 coins")
        z += 30
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    #Iron
    elif ((not metaldetector) and i > 9000 and i <= 9600) or (metaldetector and i > 10000 and i <= 15000):
        print("Iron!!, wow it's prettier than you, you gained 50 coins")
        z += 50
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    #Diamond
    elif ((not metaldetector) and i > 9600 and i <= 9998) or (metaldetector and i > 15000):
        print("DIAMONDS, wow ur so rich, you gained 150 coins")
        z += 150
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i == 9999:
        print("mr whalen??, you died to heart attack after he lowered your HOS")
        return 0
    else:
        print("mr whalen??, he raises your HOS and you gain 1000 coins")
        z += 1000
        z += 50
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z


def dungeon(a):
    i = randint(1, 10000)
    if i <= 2000:
        print("You got caught by a guard and got shot, You Die.")
        return 0
    elif i > 2000 and i <= 4000:
        print("You stepped on a spike trap, You Die.") 
        return 0
    elif i > 4000 and i <= 5000:
        print("Woah!! Diamonds, just kidding it was a fake stash, it was bombs. You Die.")
        return 0
    elif i > 5000 and i <= 6000:
        print("Woah!!, Stash of Diamonds, you gain 1000 coins.")
        a += 1000
        print(f"You have {a} gold coins.")
        deniz = input('again?')
        if deniz == "yes":
            return dungeon(a)
        return a
    elif i > 6000 and i <= 9000:
        print("WOW, a vault of gold? you gain 800 Gold.")
        a += 800
        print(f"You have {a} gold coins.")
        deniz = input('again?')
        if deniz == "yes":
            return dungeon(a)
        return a
    else:
        print("Ms.Zerega's Homework pass????, You gain 2000 Gold.")
        a += 2000
        print(f"You have {a} gold coins.")
        deniz = input('again?')
        if deniz == "yes":
            return dungeon(a)
        return a
        
        
#"Guard, 20% Rarity, You Die",
# "Spike, 20% arity, You Die.",
#"Fake Stash of Diamonds(It was bombs), 10% Rarity, You Die.",
#"Real Stash of Diamonds, 10% Rarity, Worth 1000 Gold",
#"Mr. Whalen's password (You can give yourself HOS Points),5% Rarity, Worth 1200 Gold",
#"Vault of Gold, 30% Rarity, Worth 800 Gold",
#"Ms. Zerega's Homework pass, 5% Rarity, Worth 2000 Gold"

question = input("Choose Forest, Cave, Or Dungeon: ").lower()
if question == "forest":
        x = forest(x)
if question == "cave":
     x = cave(x)
if question == "dungeon":
    x = dungeon(x)

print(f"You have {x} gold coins.")

new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps([x], indent=4)

    # Write the JSON string to the new JSON file
    f.write(json_string)



# Overwrite the old JSON file with the new one
os.remove("coins.json")
os.rename(new_file, "coins.json")