from npc import Shop
from npc import Sell

player = 0

item_Map = 750
item_Shovel = 250
item_Pickaxe = 500

item_Diamond = 150
item_Iron = 50

shopkeeper1 = Shop("Jarvis", ["Map", "Shovel", "Pickaxe"])
print(f"price: Map: {item_Map} Gold Coins, Shovel: {item_Shovel} Gold Coins, Pickaxe: {item_Pickaxe} Gold Coins")
shopkeeper1.buy("Shovel")

player1 = Sell("Eyad", ["Diamond", "Iron"])
print(f"price: Diamond: {item_Diamond} Gold Coins, Iron: {item_Iron} Gold Coins.")
player1.sell("Diamond")

player_gold_coins =- item_Shovel
print(f"You have {player_gold_coins} gold coins.")

player_gold_coins =+ item_Diamond
print(f"You have {player_gold_coins} gold coins.")