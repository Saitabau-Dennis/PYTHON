inventory = {}

def add_item(name, quantity):
    if name in inventory:
        print("The item is already in the inventory!!")
    else:
        inventory[name] = inventory.get(name,  0) + quantity
def update_item(name, quantity):
    if name in inventory:
        inventory[name] = quantity
    else:
        print("Item not found in the inventory.")
def get_item(name):
    if name in inventory:
        print(f"{name}: {inventory[name]}")
    else:
        print("Item not found in the inventory.")
def total_quantity():
    total = sum(inventory.values())
    print(f"Total quantity: {total}")


while True:
    print("Inventory System Menu")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Get Item")
    print("4. Total Quantity")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        add_item(name, quantity)
    elif choice == '2':
        name = input("Enter item name: ")
        quantity = int(input("Enter new quantity: "))
        update_item(name, quantity)
    elif choice == '3':
        name = input("Enter item name: ")
        get_item(name)
    elif choice == '4':
        total_quantity()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
