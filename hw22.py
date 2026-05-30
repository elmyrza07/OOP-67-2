import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        return "Hello!"
    def attack(self):
        return "Hero is attacking!"
    def rest(self):
        return "Hero is resting!"

class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        return "Воин атакует мечом!"

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        return "Маг кастует заклинание!"

class Assasin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        return "Ассасин атакует из-под тишка!"

warrior = Warrior("Warrior", 100, 100, 100, 100)
mage = Mage("Mage", 100, 100, 100, 100)
assasin = Assasin("Assasin", 100, 100, 100, 100)

choose = str(input("Choose your opponent: Warrior, Mage, Assasin "))
opponent = ["Warrior", "Mage", "Assasin"]
x = random.choice(opponent)
print("Your opponent is " + x)

if choose == x:
    print("Draw")
elif choose == "Warrior" and x == "Mage" or choose == "Mage" and x == "Warrior":
    print("Mage is win!")
elif choose == "Assasin" and x == "Warrior" or choose == "Warrior" and x == "Assasin":
    print("Warrior is win!")
else: print("Assasin is win!")