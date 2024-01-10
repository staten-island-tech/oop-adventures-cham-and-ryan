from npc import NPC
import json
x = open("data.json", encoding="utf8")
data = json.load(x)





player_Me = NPC("Me", "Player", [])
player_gold_coins = 10000000





def display():
    question_display = input("Do you want to view all items?")
    if question_display == "yes":
        for i in range(10):
            print(f"{i}. {data[i]['item']}")
            i += 1



def Jarvis():
    shopkeeper_Jarvis = NPC("Jarvis", "Shopkeeper", [data[0]["item"], data[3]["item"], data[6]["item"], data[7]["item"], data[8]["item"], data[10]["item"]])
    global player_gold_coins
    question_buy_Jarvis = int(input("What item number would you like to buy from Jarvis the shopkeeper?"))
    if data[question_buy_Jarvis]["price"] <= player_gold_coins:
        shopkeeper_Jarvis.sell_item(data[question_buy_Jarvis]["item"])
        player_Me.add_inventory(data[question_buy_Jarvis]["item"])
        player_gold_coins -= data[question_buy_Jarvis]["price"]
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to buy {data[question_buy_Jarvis]['item']}.")



def Brian():
    shopkeeper_Brian = NPC("Brian", "Shopkeeper", [data[1]["item"], data[2]["item"], data[4]["item"], data[9]["item"]])
    global player_gold_coins
    question_buy_Brian = int(input("What item number would you like to buy from Jarvis the shopkeeper?"))
    if data[question_buy_Brian]["price"] <= player_gold_coins:
        shopkeeper_Brian.sell_item(data[question_buy_Brian]["item"])
        player_Me.add_inventory(data[question_buy_Brian]["item"])
        player_gold_coins -= data[question_buy_Brian]["price"]
        print(f"You have {player_gold_coins} gold coins left.")
    else:
        print(f"You do not have enough gold coins to buy {data[question_buy_Brian]['item']}.")

def Ryan():
    crafter_Ryan = NPC("Ryan", "Crafter", [data[0]["variant_silver"], data[0]["variant_gold"], data[0]["variant_diamond"], data[0]["variant_emerald"]])
    global player_gold_coins
    crafter_Ryan.display()


display()
question_interact_npc = input("Who you like to interact with?")
if question_interact_npc == "Jarvis":
    Jarvis()
elif question_interact_npc == "Brian":
    Ryan()