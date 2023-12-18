from npc import Trader

import json
x = open("data.json", encoding="utf8")
data = json.load(x)

player_gold_coins = 0

def display():
    for i in range(6):
        print(f"{i + 1}. {data[i]['item']}")
        i += 1

question_display_Jarvis = input("Do you want to see Jarvis the merchant's items?").lower()
if question_display_Jarvis == "yes":
    display()

question_buy_Jarvis = input("What item number would you like to buy from Jarvis the merchant?").lower()
merchant_Jarvis = Trader("Jarvis", ["Axe", "Flashlight", "Map", "Metal Detector", "Shovel", "Pickaxe"])
merchant_Jarvis.buy_trader("Shovel")

#player_gold_coins -= item_Shovel
#print(f"You have {player_gold_coins} gold coins.")



#player1 = Trader("Eyad", ["Diamond", "Iron"])
#print(f"price: Diamond: {item_Diamond} Gold Coins, Iron: {item_Iron} Gold Coins.")
#player1.sell_trader("Diamond")
#player_gold_coins += item_Diamond
#print(f"You have {player_gold_coins} gold coins.")