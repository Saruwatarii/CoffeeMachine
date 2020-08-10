def coffee_maker(cups):
    '''
    (int) --> str(int, int, int)

    Cups gets calculated with multiplication with water, milk and coffee_beans.
    Cups can be adjusted by how much it is necessary to make the specified amount of coffee
    :param cups:
    :return: return a string with the variables multiplied with the parameter


    coffee_maker(125)
        print(f"{24000} ml of water
        {6250} ml of milk
        {1875} g of coffee beans")
    '''
    water = 200 * cups
    milk = 50 * cups
    coffee_beans = 15 * cups

    print(f"{water} ml of water\n{milk} ml of milk\n{coffee_beans} g of coffee beans")

# prompt the user
coffee_user = int(input("Write how many cups of coffee you will need: "))
# Print out the prompt and a string
print(f"For {coffee_user} of coffee you will need: ")
# Call the function coffee_maker with the argument coffee_user
coffee_maker(coffee_user)
