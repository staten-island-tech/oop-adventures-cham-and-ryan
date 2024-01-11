<<<<<<< HEAD
from npc import NPC
import json
x = open("buy.json", encoding="utf8")
buy_data = json.load(x)
y = open("buy.json", encoding="utf8")
craft_data = json.load(y)


player_Me = NPC("Me", "Player", [])
player_gold_coins = 10000000
=======
from location import Location
from random import randint 
import time, os, json
from coins import forest, cave, dungeon
from villain import Villain

x = 0
e = 5000
from datetime import datetime

now = datetime.now()

t = time.time()/86400
print(now)

with open("coins.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    x = json.load(f)[0]
>>>>>>> main





<<<<<<< HEAD
def display():
    question_display = input("Do you want to view all buyable items?")
    if question_display == "yes":
        for i in range(7):
            print(f"{i}. {buy_data[i]['item']}")
            i += 1



def interact():
    question_interact_npc = input("Who you like to interact with?")
    if question_interact_npc == "Jarvis":
        Jarvis()
    elif question_interact_npc == "Brian":
        Brian()
    elif question_interact_npc == "Ryan":
        Ryan()



def Jarvis():
    shopkeeper_Jarvis = NPC("Jarvis", "Shopkeeper", [buy_data[0]["item"], buy_data[4]["item"], buy_data[5]["item"]])
    global player_gold_coins
    question_buy_Jarvis = int(input("What item number would you like to buy from Jarvis the shopkeeper?"))
    if buy_data[question_buy_Jarvis]["price"] <= player_gold_coins:
        shopkeeper_Jarvis.sell_item(buy_data[question_buy_Jarvis]["item"])
        player_Me.add_inventory(buy_data[question_buy_Jarvis]["item"])
        player_gold_coins -= buy_data[question_buy_Jarvis]["price"]
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to buy {buy_data[question_buy_Jarvis]['item']}.")
    interact()



def Brian():
    shopkeeper_Brian = NPC("Brian", "Shopkeeper", [buy_data[1]["item"], buy_data[2]["item"], buy_data[3]["item"], buy_data[6]["item"]])
    global player_gold_coins
    question_buy_Brian = int(input("What item number would you like to buy from Brian the shopkeeper?"))
    if buy_data[question_buy_Brian]["price"] <= player_gold_coins:
        shopkeeper_Brian.sell_item(buy_data[question_buy_Brian]["item"])
        player_Me.add_inventory(buy_data[question_buy_Brian]["item"])
        player_gold_coins -= buy_data[question_buy_Brian]["price"]
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to buy {buy_data[question_buy_Brian]['item']}.")
    interact()



def Ryan():
    crafter_Ryan = NPC("Ryan", "Crafter", [craft_data[0]["item"]])
    global player_gold_coins
    question_craft_Ryan = int(input("What item number would you like to buy from Ryan the crafter?"))
    if 1000 <= player_gold_coins:
        crafter_Ryan.sell_item(craft_data[question_craft_Ryan]["item"])
        player_Me.add_inventory(craft_data[question_craft_Ryan]["item"])
        player_Me.sell_item(craft_data[question_craft_Ryan]["tool"])
        player_Me.sell_item(craft_data[question_craft_Ryan]["ore"])
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to craft {craft_data[question_craft_Ryan]['item']}")
    interact()





display()
interact()
=======
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

Eyad = Villain("Eyad(Final Boss)", "30,000 Gold")

def final():
    global x
    global e
    while x > 0 and e > 0:
        i = randint(1, 10000)
        if  i < 5000:
            x -= 2
            print (f"you have {x} gold coins")
            print (f"eyad has {e} gold coins")
        elif i >= 5000:
            e -= 2
            print (f"you have {x} gold coins")
            print (f"eyad has {e} gold coins")
    if x <= 0:
         print ("you suck and lost restart loser")
    else:
         print ("wow you beat eyad yay you win")


    

question = input("Choose Forest, Cave, Or Dungeon: ").lower()
if question == "forest":
        x = forest(x)
if question == "cave":
     x = cave(x)
if question == "dungeon":
    x = dungeon(x)

print(f"You have {x} gold coins.")

finalboss=input("do you want to fight the final boss?")
if finalboss == ("yes"):
     final()

new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps([x], indent=4)

    # Write the JSON string to the new JSON file
    f.write(json_string)



# Overwrite the old JSON file with the new one
os.remove("coins.json")
os.rename(new_file, "coins.json")

>>>>>>> main
