class Hero:
    #Конструктор класса
    def __init__(self, name, lvl, hp, skill):
        #Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.skill = skill
    def attack(self, name, lvl):
        self.name = name
        self.lvl = lvl
        print(f"Hero attacking {self.name} with level {self.lvl}.")

#Объект на основе класса
Kirito = Hero("Kirito", 100, 1000, "polymorphism")
Goblin = Kirito.attack("Goblin", 100)