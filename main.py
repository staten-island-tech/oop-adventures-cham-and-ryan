from npc import NPC
import json
x = open("buy.json", encoding="utf8")
buy_data = json.load(x)
y = open("buy.json", encoding="utf8")
craft_data = json.load(y)


player_Me = NPC("Me", "Player", [])
player_gold_coins = 10000000





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