from shop import Shop

player = 0

item_Map = 100
item_Shovel = 250
item_Pickaxe = 250

shopkeeper1 = Shop("Jarvis", ["Map", "Shovel", "Pickaxe"])
print(f"price: Map: {item_Map} Gold Coins, Shovel: {item_Shovel}, Gold Coins Pickaxe: {item_Pickaxe} Gold Coins")
shopkeeper1.sell("Shovel")

player =- item_Shovel

print(f"You have {player} gold coins.")