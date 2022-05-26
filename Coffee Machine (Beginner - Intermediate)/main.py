from info import MENU, resources, logo

COFFEE_MACHINE_BALANCE = 0


def check_resources(drink_type):
    if MENU[drink_type]["ingredients"]["water"] <= resources["water"] and \
       MENU[drink_type]["ingredients"]["coffee"] <= resources["coffee"] and \
       MENU[drink_type]["ingredients"]["milk"] <= resources["milk"]:
        return True
    return False


def process_coins(drink_type):
    global COFFEE_MACHINE_BALANCE
    print("Enter Coins:")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_entered = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    balance = total_entered - MENU[drink_type]["cost"]
    if total_entered >= MENU[drink_type]["cost"]:
        COFFEE_MACHINE_BALANCE += MENU[drink_type]["cost"]
    return balance


def make_coffee(drink_type):
    resources["water"] -= MENU[drink_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink_type]["ingredients"]["coffee"]
    resources["milk"] -= MENU[drink_type]["ingredients"]["milk"]


def print_report():
    print("Coffee Machine Resources:")
    print("Water:", str(resources["water"]) + 'ml')
    print("Milk:", str(resources["milk"]) + 'ml')
    print("Coffee:", str(resources["coffee"]) + 'g')
    print("Money:", '$' + str(COFFEE_MACHINE_BALANCE))


def coffee_machine(user_input):
    if user_input == 'off':
        print("Coffee Machine is turning off...")
    elif user_input == 'report':
        print_report()
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        if check_resources(user_input):
            user_balance = process_coins(user_input)
            if user_balance >= 0:
                make_coffee(user_input)
                print(f"Here is your {user_input} and ${round(user_balance, 2)} in change. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry, not enough resources to make", user_input)
    else:
        print("Invalid drink entered! Please try again.")


selection = ''
print(logo)
while selection != 'off':
    selection = input("\nWhich drink would you like? (espresso/latte/cappuccino): ").lower()
    coffee_machine(selection)
