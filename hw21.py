class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self, name, level):
        print( f"Привет, я {name}, мой уровень {level}.")
    def attack(self, name, strength):
        strength = strength - 1
        print (f"{name} наносит удар!")
    def rest(self, name, health):
        health = health - 1
        print (f"{name} отдыхает...")

Midoria = Hero("Midoria", 100, 100, 100)
Bakuga = Hero("Bakuga", 100, 100, 100)

Bakuga.greet("Bakuga", 100)
Bakuga.attack("Bakuga", 100)
Bakuga.rest("Bakuga", 100)


Midoria.greet("Midoria", 100)
Midoria.attack("Midoria", 100)
Midoria.rest("Midoria", 100)


