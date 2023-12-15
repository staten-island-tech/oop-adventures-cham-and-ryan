import json
x = open("data.json", encoding="utf8")
data = json.load(x)

print(data[3]["item"])

class Trader():
    def __init__(self, name, item):
        self.name = name
        self.item = item
    def buy_trader(self, buy_item):
        self.item.remove(buy_item)
        print(f"You have bought {buy_item}.")
    def sell_trader(self, sell_item):
        self.item.remove(sell_item)
        print(f"You have sold {sell_item}.")