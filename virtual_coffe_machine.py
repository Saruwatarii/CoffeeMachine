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
water = 200
milk = 50
coffee_beans = 15

water_container = int(input("Write how many ml of water the coffee machine has: "))
milk_container = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans_container = int(input("Write how many grams of coffee beans the coffee machine has: "))
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








