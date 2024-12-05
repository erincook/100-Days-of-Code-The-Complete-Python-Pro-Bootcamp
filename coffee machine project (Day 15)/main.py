#improvements (based on watching Angela's solution:
# 1. instead of enumerating the resources, you can loop through them with "for item in ingredients"
#
#for item in order_ingredients:
#   if order_ingredients[item] >= resources[item]:
#       print(f"Sorry, there is not enough {item}").
# 2. ask for coin insertion and set those variables WITHIN the coin-processing function
# 3. can loop through the deduction of ingredients when dispensing the drink, similar to 1

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def process_coins(quarters, dimes, nickels, pennies):
    """take input number of each coin, return total amount of money"""
    amount = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return amount


def check_resources(current_water, current_milk, current_coffee, user_input):
    if 'water' in MENU[user_input]['ingredients']:
        required_water = MENU[user_input]['ingredients']['water']
    else:
        required_water = 0
    if 'milk' in MENU[user_input]['ingredients']:
        required_milk = MENU[user_input]['ingredients']['milk']
    else:
        required_milk = 0
    if 'coffee' in MENU[user_input]['ingredients']:
        required_coffee = MENU[user_input]['ingredients']['coffee']
    else:
        required_coffee = 0
    if current_water >= required_water:
        if current_milk >= required_milk:
            if current_coffee >= required_coffee:
                return True
            else:
                print("Sorry, there is not enough coffee.")
                return False
        else:
            print("Sorry, there is not enough milk.")
            return False
    else:
        print("Sorry, there is not enough water.")
        return False


def check_transaction(money_inserted, user_input):
    requirements = MENU[user_input]
    required_money = requirements['cost']
    if money_inserted >= required_money:
        return True
    else:
        return False


# TODO 1a. user prompt should always reappear after a process is completed, unless the user input is "off" (DONE)
# TODO 4a. if the user puts in a prompt that is neither report, off, or a valid, drink choice, give them an error
#  and try again. (DONE)

def coffee_machine():
    """main function of the file - run the coffee machine simulation"""
    should_prompt = True
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    money_amount = 0

    while should_prompt:
        # TODO 1. prompt user for what they would like and assign it to a variable.  (DONE)
        user_choice = input("What would you like? (espresso/latte/cappuccino) ")

        # TODO 2. if input is "report", generate a report of all resource values (DONE)
        if user_choice == 'report':
            print(f'Water: {water_amount}ml')
            print(f'Milk: {milk_amount}ml')
            print(f'Coffee: {coffee_amount}g')
            print(f'Money: ${money_amount:.2f}')

        # TODO 3. if input is "off", exit the program (DONE)
        elif user_choice == 'off':
            return

        # TODO 4. if the user enters a drink choice, check to see if the resources available are sufficient.  If yes,
        #  move on to coin processing. If not, give error message. (DONE)
        elif user_choice in MENU:
            continue_to_money = check_resources(water_amount, milk_amount, coffee_amount, user_choice)

            while continue_to_money:
                # TODO 5. Process coins. Take inputs of coins, determine how much money that is. (DONE)
                print("Please insert coins.")
                number_of_quarters = int(input("How many quarters?: "))
                number_of_dimes = int(input("How many dimes?: "))
                number_of_nickels = int(input("How many nickels?: "))
                number_of_pennies = int(input("How many pennies?: "))

                money_input = process_coins(number_of_quarters, number_of_dimes, number_of_nickels, number_of_pennies)

                print(f'You have inserted ${money_input:.2f}')
                # TODO 6. Check transaction successful. Compare money put in to the item cost. If enough, dispense. If
                #  not, error. (DONE)

                enough_money = check_transaction(money_input, user_choice)

                # TODO 7. If enough resources and enough money input, dispense drink. Give feedback message.
                #  Update resources. (DONE)
                if enough_money:
                    money_amount += MENU[user_choice]['cost']
                    if money_input > MENU[user_choice]['cost']:
                        change = money_input - MENU[user_choice]['cost']
                        print(f'Here is ${change:.2f} in change.')
                    print(f'Here is your {user_choice}. Enjoy!')
                    continue_to_money = False
                    if 'water' in MENU[user_choice]['ingredients']:
                        water_amount -= MENU[user_choice]['ingredients']['water']
                    if 'milk' in MENU[user_choice]['ingredients']:
                        milk_amount -= MENU[user_choice]['ingredients']['milk']
                    if 'coffee' in MENU[user_choice]['ingredients']:
                        coffee_amount -= MENU[user_choice]['ingredients']['coffee']
                else:
                    print("That's not enough money. Try again.")
        else:
            print("That's not a valid option.")


coffee_machine()
