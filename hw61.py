from colorama import Back, Fore, Style #Эта библиотека нужна для того чтобы делать слова разных цветов
from faker import Faker #это библиотека нужна для написания ложной информации, ее используют для тестов
fake = Faker('ru_RU')

print(f"Имя: {fake.name()}")
print(f"Адрес: {fake.address()}")
print(f"Email: {fake.email()}")
print(f"Телефон: {fake.phone_number()}")
print(f"Компания: {fake.company()}")


print(Fore.RED + "Это красный текст")
print(Back.GREEN + "Это текст на зеленом фоне")
print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + "Яркий желтый текст на синем фоне")
print("Этот текст снова обычный благодаря autoreset=True")
