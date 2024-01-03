from location import Location
from random import randint 
import time, os, json
from coins import forest, cave, dungeon

x = 0

from datetime import datetime

now = datetime.now()

t = time.time()/86400
print(now)

with open("coins.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    x = json.load(f)[0]





Forest = Location("Forest", [
    "Wood, 80% Rarity", 
    "Worth 1 Gold Coin", 
    "Pre-Historic Human 20% Chance", 
    "Bear Head 20% Rarity 50 Gold Coins", 
    "Jarvis left pinky toenail 0.01% Rarity",
    "1000 Gold Coins"
    ])

# forest.information()

Cave = Location("Cave", ["Dog Feces, 20% Rarity, Worth 0 Coins",
                         "Vbucks, 30% Rarity, Worth 5 Coins"
                         "Special Miner's hat, 30% Rarity, 15 Coins",
                         "Even more Special Miner's hat, 20% Rarity, 30 Coins",
                         "Iron, 6% Rarity, Worth 50 Gold","Diamonds, 4% Rarity, Worth 150 Gold", 
                         "Mr. Whalen, 0.02% Rarity, 0.01% Chance of 1000 Coin gain"])

Dungeon = Location("Dungeon", ["Guard, 20% Rarity, You Die",
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

