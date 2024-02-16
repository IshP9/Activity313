# iteration3.py

# Iteration 2 code for getting sandwich and beverage
def get_sandwich():
    print("Welcome to the sandwich shop!")
    print("Menu:")
    print("1. Chicken - $5.25")
    print("2. Beef - $6.25")
    print("3. Tofu - $5.75")
    
    choice = int(input("Please select a sandwich (1 for Chicken, 2 for Beef, 3 for Tofu): "))
    price = 0
    
    if choice == 1:
        print("You selected Chicken.")
        price = 5.25
    elif choice == 2:
        print("You selected Beef.")
        price = 6.25
    elif choice == 3:
        print("You selected Tofu.")
        price = 5.75
    else:
        print("Invalid selection.")
    
    return price

def get_beverage():
    print("Would you like a beverage? (yes/no): ")
    choice = input().lower()
    price = 0
    
    if choice == 'yes':
        print("Beverage Sizes:")
        print("1. Small - $1.00")
        print("2. Medium - $1.75")
        print("3. Large - $2.25")
        
        size = int(input("Please select a size (1 for Small, 2 for Medium, 3 for Large): "))
        
        if size == 1:
            print("You selected Small.")
            price = 1.00
        elif size == 2:
            print("You selected Medium.")
            price = 1.75
        elif size == 3:
            print("You selected Large.")
            price = 2.25
        else:
            print("Invalid size.")
    
    else:
        print("No beverage selected.")
    
    return price

# Iteration 3 code for getting fries
def get_fries():
    print("Would you like fries? (yes/no): ")
    choice = input().lower()
    price = 0
    
    if choice == 'yes':
        print("French Fry Sizes:")
        print("1. Small - $1.00")
        print("2. Medium - $1.50")
        print("3. Large - $2.00")
        
        size = int(input("Please select a size (1 for Small, 2 for Medium, 3 for Large): "))
        
        if size == 1:
            print("You selected Small.")
            price = 1.00
        elif size == 2:
            print("You selected Medium.")
            price = 1.50
        elif size == 3:
            print("You selected Large.")
            price = 2.00
        else:
            print("Invalid size.")
    
    else:
        print("No fries selected.")
    
    return price

# Main code for Iteration 3
sandwich_price = get_sandwich()
beverage_price = get_beverage()
fries_price = get_fries()
total_cost = sandwich_price + beverage_price + fries_price
print("Total cost: $", total_cost)
