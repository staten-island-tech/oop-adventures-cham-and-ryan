class Shop():
    def __init__(self, name, item):
        self.name = name
        self.item = item
    def sell(self, sold_item):
        print(self.item)
        print("What would you like to buy?")
        self.item.remove(sold_item)
        print(f"You have purchased {sold_item}")