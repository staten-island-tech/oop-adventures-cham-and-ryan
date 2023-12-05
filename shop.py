class Shop():
    def __init__(self, name, item, price):
        self.name = name
        self.item = item
        self.item = price
    def sell(self, sold):
        self.item.remove(sold)
        print(f"You have purchased {sold}")
        print(self.item)
    def information(self):
        print(self.price)