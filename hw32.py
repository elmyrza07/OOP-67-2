from abc import ABC, abstractmethod

class Hero():
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.__health = health
    def greet(self, name, level):
        print(f"Привет, я {name}, мой уровень {self.level}!")
    def rest(self, name, __health):
        print( f"{name} отдыхает!")
        __health = __health + 1
    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом")

class Assasin(Hero):
    def attack(self):
        print("Ассасин атакует из-под тишка")

class Mage(Hero):
    def attack(self):
        print("Маг использует магию")


war = Warrior("Eren", 100, 100)
mage = Mage("Friren", 100, 100)
assasin = Assasin("Loid", 100, 100)

war.greet("Eren", 100)
mage.greet("Friren", 100)
assasin.greet("Loid", 100)

war.rest("Eren", 100)
mage.rest("Friren", 100)
assasin.rest("Loid", 100)

war.attack()
mage.attack()
assasin.attack()