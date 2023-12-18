from npc import Trader

import json
x = open("data.json", encoding="utf8")
data = json.load(x)

player_gold_coins = 0

item_Map = 750
item_Shovel = 250
item_Pickaxe = 500

item_Diamond = 150
item_Iron = 50

shopkeeper1 = Trader("Jarvis", ["Map", "Shovel", "Pickaxe"])
print(data[1]["item"])
shopkeeper1.buy_trader("Shovel")

player_gold_coins -= item_Shovel
print(f"You have {player_gold_coins} gold coins.")



#player1 = Trader("Eyad", ["Diamond", "Iron"])
#print(f"price: Diamond: {item_Diamond} Gold Coins, Iron: {item_Iron} Gold Coins.")
#player1.sell_trader("Diamond")
#player_gold_coins += item_Diamond
#print(f"You have {player_gold_coins} gold coins.")

