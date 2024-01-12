import random


flashlight = False
metaldetector = False
shovel = False


Equip = input("What item do you want to use?(the ones you have dont lie):")


if Equip == "metaldetector":
    metaldetector = True
    if metaldetector == True:
        print("Metaldetector:True")
elif Equip == "shovel":
    shovel = True

elif Equip == "None":
    
    flashlight = False
    metaldetector = False


def forest(y):
    i = random.randint(1, 10000)

    if i <= 5000:

        print("Wow you have a lot of wood, I'll give you 1 gold coin for them", )

        y += 1

        print(f"You have {y} gold coins.")

        ryan = input('again?')

        if ryan == "yes":
            return forest(y)

        return y
    
    elif i > 5000 and i <= 7000:
        print("you got brutally stabbed to death and died while looking at your heart on the ground")
        
        return 0
    
    elif i > 7000 and i <= 9999:
        print("is that a bear head i see so sigma")
        y += 35
        print(f"You have {y} gold coins.")
        ryan = input('again?')

        if ryan == "yes":
            return forest(y)

        return y
    
    else:
        print("woah sir thats a nice toenail, i bet it's jarvis'")
        y += 1000
        print(f"You have {y} gold coins.")
        ryan = input('again?')

        if ryan == "yes":
            return forest(y)

        return y

def cave(z):

    i = random.randint(1, 10000)
    if metaldetector:
        i = random.randint (1, 20000)
    if shovel:
        i = random.randint (1, 10000)
    if ((not shovel) and i < 2000) or (shovel and i < 1000):
        print("wow, you found dog feces. you gained 0 coins")
        z += 0
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i >= 2000 and i < 5000:
        print("VBUCKS!!, you gained 5 Gold Coins")
        z += 5
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i > 5000 and i <= 6000:
        print("Wow, you found special miner's hat, you gained 15 coins")
        z += 15
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i>6000 and i <= 7000:
        print("You unfortunately died to rock collapse")
        
        return 0
    elif i > 7000 and i <= 9000:
        print("Wow, you found the even more special miner's hat, you gained 30 coins")
        z += 30
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    #Iron
    elif ((not metaldetector) and i > 9000 and i <= 9600) or (metaldetector and i > 10000 and i <= 15000):
        print("Iron!!, wow it's prettier than you, you gained 50 coins")
        z += 50
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    #Diamond
    elif ((not metaldetector) and i > 9600 and i <= 9998) or (metaldetector and i > 15000):
        print("DIAMONDS, wow ur so rich, you gained 150 coins")
        z += 150
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z
    elif i == 9999:
        print("mr whalen??, you died to heart attack after he lowered your HOS")
        return 0
    else:
        print("mr whalen??, he raises your HOS and you gain 1000 coins")
        z += 1000
        z += 50
        print(f"You have {z} gold coins.")
        cham = input('again?')
        if cham == "yes":
            return cave(z)
        return z


def dungeon(a):
    i = random.randint(1, 10000)
    if axe:
        i = random.randint(2001, 10000)
    if i <= 2000:
        print("You got caught by a guard and got shot, You Die.")
        return 0
    elif i > 2000 and i <= 4000:
        print("You stepped on a spike trap, You Die.") 
        return 0
    elif i > 4000 and i <= 5000:
        print("Woah!! Diamonds, just kidding it was a fake stash, it was bombs. You Die.")
        return 0
    elif i > 5000 and i <= 6000:
        print("Woah!!, Stash of Diamonds, you gain 1000 coins.")
        a += 1000
        print(f"You have {a} gold coins.")
        deniz = input('again?')
        if deniz == "yes":
            return dungeon(a)
        return a
    elif i > 6000 and i <= 9000:
        print("WOW, a vault of gold? you gain 800 Gold.")
        a += 800
        print(f"You have {a} gold coins.")
        deniz = input('again?')
        if deniz == "yes":
            return dungeon(a)
        return a
    else:
        print("Ms.Zerega's Homework pass????, You gain 2000 Gold.")
        a += 2000
        print(f"You have {a} gold coins.")
        deniz = input('again?')
        if deniz == "yes":
            return dungeon(a)
        return a