# Logic, Arithmetic Operators, and Conditionals

def get_ketchup():
    print("How many ketchup packets would you like? ")
    packets = int(input())
    price = packets * 0.25
    return price

sandwich_price = get_sandwich()
beverage_price = get_beverage()
fries_price = get_fries()
ketchup_price = get_ketchup()

total_cost = sandwich_price + beverage_price + fries_price + ketchup_price
if sandwich_price != 0 and beverage_price != 0 and fries_price != 0:
    total_cost -= 1  # Apply $1 discount if all main items selected

print("Total cost: $", total_cost)
