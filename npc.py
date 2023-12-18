class Trader():
    def __init__(self, name, item):
        self.name = name
        self.item = item
    def buy_trader(self, buy_item):
        self.item.remove(buy_item)
        print(f"You have bought a {buy_item} from {self.name}.")
    def sell_trader(self, sell_item):
        self.item.remove(sell_item)
        print(f"You have sold a {sell_item} to {self.name}.")