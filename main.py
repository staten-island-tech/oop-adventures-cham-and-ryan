from npc import Trader

import json
x = open("data.json", encoding="utf8")
data = json.load(x)

def display():
    for i in range(6):
        print(f"{i}. {data[i]['item']}")
        i += 1

def Jarvis_the_merchant():
    player_gold_coins = 0
    merchant_Jarvis = Trader("Jarvis", [data[0]["item"], data[4]["item"], data[7]["item"], data[8]["item"], data[9]["item"], data[11]["item"]])
    
    question_display_Jarvis = input("Do you want to see Jarvis the merchant's items?").lower()
    if question_display_Jarvis == "yes":
        display()

    question_buy_Jarvis = int(input("What item number would you like to buy from Jarvis the merchant?"))
    if data[question_buy_Jarvis]["price"] <= player_gold_coins:
        merchant_Jarvis.buy_trader(data[question_buy_Jarvis]["item"])
        player_gold_coins -= data[question_buy_Jarvis]["price"]
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to buy {data[question_buy_Jarvis]['item']}.")

question_interact_Jarvis = input("Would you like to interact with Jarvis the merchant?").lower()
if question_interact_Jarvis == "yes":
    Jarvis_the_merchant()

def Jarvis_brother_the_merchant():
    player_gold_coins = 0
    merchant_Jarvis_brother = Trader("Jarvis' brother", [data[1]["item"], data[2]["item"], data[3]["item"], data[5]["item"], data[6]["item"], data[10]["item"], data[12]["item"]])

#player_gold_coins -= item_Shovel
#print(f"You have {player_gold_coins} gold coins.")



#player1 = Trader("Eyad", ["Diamond", "Iron"])
#print(f"price: Diamond: {item_Diamond} Gold Coins, Iron: {item_Iron} Gold Coins.")
#player1.sell_trader("Diamond")
#player_gold_coins += item_Diamond
#print(f"You have {player_gold_coins} gold coins.")