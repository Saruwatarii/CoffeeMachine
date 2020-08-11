'''
def coffee_maker(cups):

    (int) --> str(int, int, int)

    Cups gets calculated with multiplication with water, milk and coffee_beans.
    Cups can be adjusted by how much it is necessary to make the specified amount of coffee
    :param cups:
    :return: return a string with the variables multiplied with the parameter


    coffee_maker(125)
        print(f"{24000} ml of water
        {6250} ml of milk
        {1875} g of coffee beans")

    water = 200 * cups
    milk = 50 * cups
    coffee_beans = 15 * cups

    print(f"{water} ml of water\n{milk} ml of milk\n{coffee_beans} g of coffee beans")

coffee_user = int(input("Write how many cups of coffee you will need: "))

print(f"For {coffee_user} of coffee you will need: ")

coffee_maker(coffee_user)
'''
#-------------------------------------------------------------------------------------------------------


def coffe_overview(water, milk, bean, cup, money):
    print(f"The coffee machine has:\n"
          f"{water_machine} of water\n"
          f"{milk_machine} of milk\n"
          f"{bean_machine} of coffee beans\n"
          f"{cups_machine} of disposable cups\n"
          f"{money_machine} of money\n")

'''
water = 200
milk = 50
coffee_beans = 15
'''
# Default coffee machine settings
water_machine = 400
milk_machine = 540
bean_machine = 120
cups_machine = 9
money_machine = 550

# Cost of different types of coffee
espresso = 4
latte = 7
cappuccino = 6

coffe_overview(water_machine, milk_machine, bean_machine, cups_machine, money_machine)
starter_menu = input("Write action (buy, fill, take): ").lower()

if starter_menu == "buy":
    type_coffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if type_coffee == 1:
        money_machine += espresso
        water_machine = water_machine - 250
        bean_machine = bean_machine - 16
        cups_machine = cups_machine - 1
        print()
        coffe_overview(water_machine, milk_machine, bean_machine, cups_machine, money_machine)
    elif type_coffee == 2:
        money_machine += latte
        water_machine = water_machine - 350
        milk_machine = milk_machine - 75
        bean_machine = bean_machine - 12
        cups_machine = cups_machine - 1
        print()
        coffe_overview(water_machine, milk_machine, bean_machine, cups_machine, money_machine)
    else:
        money_machine += cappuccino
        water_machine = water_machine - 200
        milk_machine = water_machine - 100
        bean_machine = bean_machine -12
        cups_machine = cups_machine - 1
        print()
        coffe_overview(water_machine, milk_machine, bean_machine, cups_machine, money_machine)


elif starter_menu == "fill":
    water_container = int(input("Write how many ml of water do you want to add: "))
    milk_container = int(input("Write how many ml of milk do you want to add: "))
    coffee_beans_container = int(input("Write how many grams of coffee beans do you want to add: "))
    disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    water_machine += water_container
    milk_machine += milk_container
    bean_machine += coffee_beans_container
    cups_machine += disposable_cups

    coffe_overview(water_machine, milk_machine, bean_machine, cups_machine, money_machine)

elif starter_menu == "take":
    print(f"I gave you ${money_machine}\n")
    money_machine -= money_machine
    coffe_overview(water_machine, milk_machine, bean_machine, cups_machine, money_machine)



'''
many_cups_coffee = int(input("Write how many cups of coffee you will need: "))
# How many cups of each ingredient its in the container
water_cup =  water_container // water
milk_cup = milk_container // milk
coffe_bean_cup = coffee_beans_container // coffee_beans
# Find the total cup of coffee from ingredients
possible_coffee_cups = min(water_cup, milk_cup, coffe_bean_cup)

if possible_coffee_cups < many_cups_coffee:
    print(f"No, I can make only {possible_coffee_cups} cups of coffee")
elif possible_coffee_cups == many_cups_coffee:
    print("Yes, I can make that amount of coffee")
else:
    print(f"Yes, I can make that amount of coffee (and even {possible_coffee_cups - many_cups_coffee} more than that)")
'''







