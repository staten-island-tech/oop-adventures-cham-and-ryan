class NPC():
    def __init__(self, name, occupation, item):
        self.name = name
        self.occupation = occupation
        self.item = item
    def add_inventory(self, add_item):
        self.item.append(add_item)
        print(f"A {add_item} has been added into your inventory.")
    def sell_item(self, sell_item):
        self.item.remove(sell_item)
        print(f"{self.name} has sold a {sell_item} to you.")
    def display(self):
        print(self.item)