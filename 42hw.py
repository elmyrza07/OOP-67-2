class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self, rates: dict):
        return self.amount * rates[self.currency]

    def __add__(self, other):
        x = self.convert_to_kgs(rates)
        y = other.convert_to_kgs(rates)
        return Money(x + y, "KGS")

    def __sub__(self, other):
        s1 = 0
        s2 = 0
        self.convert_to_kgs(rates)
        other.convert_to_kgs(rates)
        retuen = Money(s1 - s2, "KGS")
    def __mul__(self, other):
        return self.amount * other
    def __truediv__(self, other):
        return self.amount / other
    def __str__(self):
        return str(self.amount) + " KGS"
rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result = money1 + money2

print(result)