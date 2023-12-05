from shop import Shop

player = 0

item_Map = 100
item_Shovel = 500
item_Pickaxe = 500

shopkeeper1 = Shop("Jarvis", ["Map: 100 Gold Coins", "Shovel: 500 Gold Coins", "Pickaxe: 500 Gold Coins"])
shopkeeper1.sell("Shovel") 
player -= item_Shovel
print(player)