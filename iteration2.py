# iteration2.py

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

if __name__ == "__main__":
    from iteration1 import get_sandwich
    
    sandwich_price = get_sandwich()
    beverage_price = get_beverage()
    total_cost = sandwich_price + beverage_price
    print("Total cost so far: $", total_cost)
