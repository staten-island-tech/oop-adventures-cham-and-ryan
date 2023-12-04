class Shop():
    def __init__(self, name, item):
        self.name = name
        self.item = item
    def sell(self, sold):
        self.products.remove(sold)
        print(f"You have purchased {sold}")
        print(self.item)