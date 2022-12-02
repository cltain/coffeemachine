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
}


def enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item} ≧ ﹏ ≦.")
            print("Enter 'off'")
            return False
    return True


def coins(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if total < cost:
        print("Sorry, that is not enough money 😖. Money refunded.")
        return False
    elif total > cost:
        print(f"Here is ${round((total - cost), 2)} in change.")
        return True
    return True


def deplete(drink_name, ingredient_items):
    for item in ingredient_items:
        resources[item] -= ingredient_items[item]
    print(f"Here is your {drink_name} ☕! Enjoy! ☆*: .｡. o(≧▽≦)o .｡.:*☆")


total_money = 0
make_coffee = True
while make_coffee:
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    coffee_type = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}\nMoney: ${total_money}")
    elif coffee_type == "off":
        make_coffee = False
    else:
        drink = MENU[coffee_type]
        if enough(drink["ingredients"]):
            if coins(drink["cost"]):
                deplete(coffee_type, drink["ingredients"])
                total_money += drink["cost"]
