# Algorithms, Variables, Procedures, Strings and Concatenation, and Relational Operators

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

sandwich_price = get_sandwich()
print("Total cost so far: $", sandwich_price)
