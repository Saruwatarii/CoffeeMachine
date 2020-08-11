import sys

BUY = "buy"
FILL = "fill"
TAKE = "take"
REMAINING = "remaining"
EXIT = "exit"

# Default coffee machine settings
water_machine = 400
milk_machine = 540
bean_machine = 120
cups_machine = 9
money_machine = 550

def enough_coffe():
    print("I have enough resources, making you a coffee!")

def format():
    print()

def coffe_overview(water, milk, bean, cup, money):
    if money != 0:
        print(f"The coffee machine has:\n"
              f"{water_machine} of water\n"
              f"{milk_machine} of milk\n"
              f"{bean_machine} of coffee beans\n"
              f"{cups_machine} of disposable cups\n"
              f"${money_machine} of money\n")
    else:
        print(f"The coffee machine has:\n"
              f"{water_machine} of water\n"
              f"{milk_machine} of milk\n"
              f"{bean_machine} of coffee beans\n"
              f"{cups_machine} of disposable cups\n"
              f"{money_machine} of money\n")

def espresso(water, milk, bean, cups, money):
    espresso = 4
    global money_machine, water_machine, bean_machine, cups_machine, milk_machine
    if water_machine >= 250 and bean_machine >= 16:
        water_machine = water_machine - 250
        bean_machine = bean_machine - 16
        cups_machine = cups_machine - 1
        money_machine += espresso

        enough_coffe()
        format()
    else:
        remaining_ingredients(water, milk, bean)
        format()

def latte(water, milk, bean, cups, money):
    latte = 7
    global money_machine, water_machine, bean_machine, cups_machine, milk_machine
    if water_machine >= 350 and milk_machine >= 75 and bean_machine >= 12:
        water_machine = water_machine - 350
        milk_machine = milk_machine - 75
        bean_machine = bean_machine - 12
        cups_machine = cups_machine - 1
        money_machine += latte

        enough_coffe()
        format()
    else:
        remaining_ingredients(water, milk, bean)
        format()

def cappuccino(water, milk, bean, cups, money):
    cappuccino = 6
    global money_machine, water_machine, bean_machine, cups_machine, milk_machine
    if water_machine >= 200 and milk_machine >= 100 and bean_machine >= 12:
        water_machine = water_machine - 200
        milk_machine = milk_machine - 100
        bean_machine = bean_machine - 12
        cups_machine = cups_machine - 1
        money_machine += cappuccino

        enough_coffe()
        format()
    else:
        remaining_ingredients(water, milk, bean)
        format()

def fill_machine(water, milk, beans, cups):
    global water_machine, bean_machine, cups_machine, milk_machine
    format()
    water_container = int(input("Write how many ml of water do you want to add:\n"))
    milk_container = int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans_container = int(input("Write how many grams of coffee beans do you want to add:\n"))
    disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

    water_machine += water_container
    milk_machine += milk_container
    bean_machine += coffee_beans_container
    cups_machine += disposable_cups
    format()

def remaining_ingredients(water, milk, bean):
    if water <= 249:
        print(f"Sorry, not enough water!")
        format()
        main()
    elif milk <= 74:
        print(f"Sorry, not enough milk!")
        main()
        format()
    elif bean <= 11:
        print(f"Sorry, not enough coffee beans!")
        format()
        main()

def main():
    global money_machine
    flag = True

    while flag:
        starter_menu = input("Write action (buy, fill, take, remaining, exit):\n")

        if starter_menu == BUY:
            format()
            type_coffee = (
                input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))

            if type_coffee == str(1):
                espresso(water_machine, milk_machine, bean_machine, cups_machine, money_machine)

            elif type_coffee == str(2):
                latte(water_machine, milk_machine, bean_machine, cups_machine, money_machine)

            elif type_coffee == str(3):
                cappuccino(water_machine, milk_machine, bean_machine, cups_machine, money_machine)

            elif type_coffee == "back":
                format()
                main()

        elif starter_menu == FILL:
            fill_machine(water_machine, milk_machine, bean_machine, cups_machine)

        elif starter_menu == TAKE:
            format()
            print(f"I gave you ${money_machine}\n")
            money_machine -= money_machine

        elif starter_menu == REMAINING:
            format()
            coffe_overview(water_machine, milk_machine, bean_machine, cups_machine, money_machine)

        elif starter_menu == EXIT:
            sys.exit()
            
main()