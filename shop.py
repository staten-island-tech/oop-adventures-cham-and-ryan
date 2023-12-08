class Shop():
    def __init__(self, name, item):
        self.name = name
        self.item = item
    def sell(self, sold_item):
        self.item.remove(sold_item)
        print(f"You have purchased {sold_item}")