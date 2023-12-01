from location import Location
from random import randint

forest = Location("Forest", ["Wood", "Sapling", "Bear Head", "Jarvis' left pinky toenail"])
forest.information()

cave = Location("Cave", ["Diamonds", "Iron", "Mr. Whalen", "Special Miner's hat", "Even more Special Miner's hat", "Dog Feces"])
cave.information()

i = randint(1, 10000)
if i <= 8000:
    print("thats a lot of wood sir")
if i > 8000 and i <= 9500:
    print("haha baby tree sapling")
if i > 9500 and i <= 9999:
    print("is that a bear head i see so sigma")
if i == 10000:
    print("woah sir thats a nice toenail, i bet it's jarvis'")