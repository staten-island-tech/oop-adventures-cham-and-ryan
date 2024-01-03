from npc import Trader

import json
x = open("data.json", encoding="utf8")
data = json.load(x)

player_gold_coins = 10000000

def display():
    question_display = input("Do you want to see all buyable items?")
    if question_display == "yes":
        for i in range(12):
            print(f"{i}. {data[i]['item']}")
            i += 1

display()

def Jarvis():
    merchant_Jarvis = Trader("Jarvis", [data[0]["item"], data[3]["item"], data[6]["item"], data[7]["item"], data[8]["item"], data[10]["item"]])
    
    global player_gold_coins
    
    question_buy_Jarvis = int(input("What item number would you like to buy from Jarvis the merchant?"))
    if data[question_buy_Jarvis]["price"] <= player_gold_coins:
        merchant_Jarvis.buy_trader(data[question_buy_Jarvis]["item"])
        player_gold_coins -= data[question_buy_Jarvis]["price"]
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to buy {data[question_buy_Jarvis]['item']}.")



def Brian():
    merchant_Brian = Trader("Brian", [data[1]["item"], data[2]["item"], data[4]["item"], data[5]["item"], data[9]["item"], data[11]["item"]])
    
    global player_gold_coins
    
    question_buy_Brian = int(input("What item number would you like to buy from Jarvis the merchant?"))
    if data[question_buy_Brian]["price"] <= player_gold_coins:
        merchant_Brian.buy_trader(data[question_buy_Brian]["item"])
        player_gold_coins -= data[question_buy_Brian]["price"]
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to buy {data[question_buy_Brian]['item']}.")



question_interact_npc = input("Who you like to interact with?")
if question_interact_npc == "Jarvis":
    Jarvis()
elif question_interact_npc == "Brian":
    Brian()