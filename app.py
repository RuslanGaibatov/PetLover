import time
import random


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0 (голоден) до 100 (сыт)
        self.happiness = 50  # 0 (грустный) до 100 (счастливый)
        self.energy = 50  # 0 (устал) до 100 (бодр)
        self.is_alive = True

    def feed(self):
        if not self.is_alive:
            print(f"{self.name} больше не может есть.")
            return
        self.hunger = min(self.hunger + 20, 100)
        self.happiness = min(self.happiness + 5, 100)
        print(f"Ты покормил {self.name}. Теперь его голод {self.hunger}, счастье {self.happiness}.")

    def play(self):
        if not self.is_alive:
            print(f"{self.name} больше не может играть.")
            return
        if self.energy < 20:
            print(f"{self.name} слишком устал для игры.")
        else:
            self.hunger = max(self.hunger - 10, 0)
            self.happiness = min(self.happiness + 15, 100)
            self.energy = max(self.energy - 20, 0)
            print(
                f"Ты поиграл с {self.name}. Теперь его голод {self.hunger}, счастье {self.happiness}, энергия {self.energy}.")

    def sleep(self):
        if not self.is_alive:
            print(f"{self.name} больше не может спать.")
            return
        self.energy = min(self.energy + 40, 100)
        self.hunger = max(self.hunger - 10, 0)
        print(f"{self.name} поспал. Теперь его энергия {self.energy}, голод {self.hunger}.")

    def status(self):
        if not self.is_alive:
            return f"{self.name} мертв. :( Пожалуйста, перезапусти игру, чтобы начать заново."
        return f"Состояние {self.name}: Голод: {self.hunger}, Счастье: {self.happiness}, Энергия: {self.energy}."

    def update(self):
        """Метод для обновления состояния питомца со временем."""
        if not self.is_alive:
            return
        self.hunger = max(self.hunger - random.randint(1, 5), 0)
        self.happiness = max(self.happiness - random.randint(1, 3), 0)
        self.energy = max(self.energy - random.randint(1, 4), 0)

        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0:
            self.is_alive = False
            print(f"{self.name} умер от нехватки внимания. :(")


def main():
    print("Добро пожаловать в игру 'Электронный питомец'!")
    pet_name = input("Как ты назовешь своего питомца? ")
    pet = Pet(pet_name)

    actions = {
        "1": pet.feed,
        "2": pet.play,
        "3": pet.sleep,
        "4": lambda: print(pet.status())
    }

    while pet.is_alive:
        print("\nВыбери действие:")
        print("1. Покормить")
        print("2. Поиграть")
        print("3. Положить спать")
        print("4. Проверить состояние")
        print("5. Выйти")

        choice = input(">> ").strip()

        if choice == "5":
            print("Спасибо за игру! До свидания!")
            break
        elif choice in actions:
            actions[choice]()
            pet.update()
            time.sleep(1)
        else:
            print("Пожалуйста, выбери правильный номер действия.")


if __name__ == "__main__":
    main()
