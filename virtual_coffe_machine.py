import sys

class CoffeeMachine():
    water_machine = 400
    milk_machine = 540
    bean_machine = 120
    cups_machine = 9
    money_machine = 550
    BUY = "buy"
    FILL = "fill"
    TAKE = "take"
    REMAINING = "remaining"
    EXIT = "exit"

    def menu(self):
        starter_menu = input("Write action (buy, fill, take, remaining, exit):\n")
        if starter_menu == CoffeeMachine.BUY:
            self.buy()
        elif starter_menu == CoffeeMachine.FILL:
            self.fill()
            self.menu()
        elif starter_menu == CoffeeMachine.TAKE:
            print()
            print(f"I gave you ${CoffeeMachine.money_machine}\n")
            CoffeeMachine.money_machine -= CoffeeMachine.money_machine
            self.menu()
        elif starter_menu == CoffeeMachine.REMAINING:
            self.coffe_overview()
            self.menu()
        elif starter_menu == CoffeeMachine.EXIT:
            sys.exit()

    def buy(self):
        print()
        type_coffee = (
            input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
        if type_coffee == str(1):
            self.espresso()
            self.menu()
        elif type_coffee == str(2):
            self.latte()
            self.menu()
        elif type_coffee == str(3):
            self.cappuccino()
            self.menu()
        elif type_coffee == "back":
            self.menu()

    def fill(self):
        print()
        CoffeeMachine.water_machine += int(input("Write how many ml of water do you want to add:\n"))
        CoffeeMachine.milk_machine += int(input("Write how many ml of milk do you want to add:\n"))
        CoffeeMachine.bean_machine += int(input("Write how many grams of coffee beans do you want to add:\n"))
        CoffeeMachine.cups_machine += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print()
        self.menu()

    def enough_coffe(self):
        print("I have enough resources, making you a coffee!\n")

    def coffe_overview(self):
        print()
        print(f"The coffee machine has:\n"
                f"{CoffeeMachine.water_machine} of water\n"
                f"{CoffeeMachine.milk_machine} of milk\n"
                f"{CoffeeMachine.bean_machine} of coffee beans\n"
                f"{CoffeeMachine.cups_machine} of disposable cups\n"
                f"${CoffeeMachine.money_machine} of money")
        print()

    def remaining_ingredients(self):
        if CoffeeMachine.water_machine <= 249:
            print(f"Sorry, not enough water!\n")
            self.menu()
        elif CoffeeMachine.milk_machine <= 74:
            print(f"Sorry, not enough milk!\n")
            self.menu()
        elif CoffeeMachine.bean_machine <= 11:
            print(f"Sorry, not enough coffee beans!\n")
            self.menu()

    def cappuccino(self):
        cappuccino = 6
        if CoffeeMachine.water_machine >= 200 and CoffeeMachine.milk_machine >= 100 and CoffeeMachine.bean_machine >= 12:
            CoffeeMachine.water_machine -= 200
            CoffeeMachine.milk_machine -= 100
            CoffeeMachine.bean_machine -= 12
            CoffeeMachine.cups_machine -= 1
            CoffeeMachine.money_machine += cappuccino
            self.enough_coffe()
        else:
            self.remaining_ingredients()

    def espresso(self):
        espresso = 4
        if CoffeeMachine.water_machine >= 250 and CoffeeMachine.bean_machine >= 16:
            CoffeeMachine.water_machine -= 250
            CoffeeMachine.bean_machine -= 16
            CoffeeMachine.cups_machine -= 1
            CoffeeMachine.money_machine += espresso
            self.enough_coffe()
        else:
            self.remaining_ingredients()

    def latte(self):
        latte = 7
        if CoffeeMachine.water_machine >= 350 and CoffeeMachine.milk_machine >= 75 and CoffeeMachine.bean_machine >= 12:
            CoffeeMachine.water_machine -= 350
            CoffeeMachine.milk_machine -= 75
            CoffeeMachine.bean_machine -= 12
            CoffeeMachine.cups_machine -= 1
            CoffeeMachine.money_machine += latte
            self.enough_coffe()
        else:
            self.remaining_ingredients()

user = CoffeeMachine()
user.menu()













