class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

class Mage(Hero):
    def __init__(self, name, lvl, hp, mp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = mp
    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")

class Warrior(Mage):
    def __init__(self, name, lvl, hp, mp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = mp
    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")

class BankAccount():
    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = "Simbank"
    def login(self, password):
        self.__password = "password"
    def full_info(self):
        return (f"Имя: {self.hero.name} \n Класс: {type(self.hero)} \n Баланс: {self._balance}")
    def get_bank_name(self):
        return (self.bank_name)
    def bonus_for_level(self):
        return (self.hero.lvl*10)

    def __str__(self):
        return (f"{self.hero.name}|Баланс:{self._balance} SOM")
    def __add__(self, other):
        if (type(self.hero) == type(other.hero) == Mage):
            return (f"Сумма счетов двух магов: {self._balance + other._balance}")
        elif (type(self.hero) == type(other.hero) == Warrior):
            return (f"Сумма счетов двух воителей: {self._balance + other._balance}")
        else: return ("Ошибка: Нельзя сложить счета двух героев разных классов!")
    def __eq__(self, other):
        klass = type(self.hero) == type(other.hero)
        leveel = self.hero.lvl == other.hero.lvl
        return(klass)
        return(leveel)

merlin = Mage("Mage", 10, 10, 10)
friren = Mage("Mage", 10, 10, 10)
eren = Warrior("Warrior", 10, 10, 10)
naruto = Warrior("Warrior", 10, 10, 10)

acc1 = BankAccount(merlin, 3000, "iammage")
acc2 = BankAccount(friren, 10000, "elf112")
acc3 = BankAccount(eren, 100000, "titan04")
acc4 = BankAccount(naruto, 100000, "naruto123")

merlin.action()
friren.action()
eren.action()
naruto.action()

print(acc1)
print(acc2)
print(acc3)
print(acc4)

print(acc1.get_bank_name())
print(acc2.bonus_for_level())
print(acc1.full_info())
print(acc3+acc4)
print(acc4+acc1)

print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)




