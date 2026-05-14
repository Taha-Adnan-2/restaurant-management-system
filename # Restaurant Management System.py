# Restaurant Management System

# Global variables
menu = []  # List to store menu items
orders = []  # List to store orders
inventory = []  # List to store inventory items

def show_current_menu():
    print("\n=== Current Menu ===")
    if len(menu) == 0:
        print("Menu is empty!")
        return
    
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i][0]} - ${menu[i][2]}")

def show_menu():
    print("\n=== Current Menu ===")
    if len(menu) == 0:
        print("Menu is empty!")
        return
    
    for i in range(len(menu)):
        print(f"\n{i+1}. {menu[i][0]}")
        print(f"   Category: {menu[i][1]}")
        print(f"   Price: ${menu[i][2]}")
        print(f"   Ingredients: {', '.join(menu[i][3])}")

def add_dish():
    print("\n=== Add New Dish ===")
    name = input("Enter dish name: ")
    category = input("Enter category (Appetizer/Main Course/Dessert/Beverage): ")
    price = float(input("Enter price: "))
    
    # Get ingredients
    ingredients = []
    print("Enter ingredients (type 'done' when finished):")
    ingredient = input("Ingredient: ")
    while ingredient.lower() != 'done':
        ingredients.append(ingredient)
        ingredient = input("Ingredient: ")
    
    # Create dish entry
    dish = [name, category, price, ingredients]
    menu.append(dish)
    print(f"\nDish '{name}' added successfully!")

def update_dish():
    print("\n=== Update Dish ===")
    show_current_menu()
    if len(menu) == 0:
        return
        
    name = input("\nEnter dish name to update: ")
    
    # Find dish
    found = False
    for i in range(len(menu)):
        if menu[i][0] == name:
            found = True
            print("\nCurrent details:")
            print(f"Name: {menu[i][0]}")
            print(f"Category: {menu[i][1]}")
            print(f"Price: ${menu[i][2]}")
            print(f"Ingredients: {', '.join(menu[i][3])}")
            
            # Update details
            print("\nEnter new details (press Enter to keep current value):")
            new_name = input("New name: ")
            new_category = input("New category: ")
            new_price = input("New price: ")
            
            # Update only if new values are provided
            if new_name:
                menu[i][0] = new_name
            if new_category:
                menu[i][1] = new_category
            if new_price:
                menu[i][2] = float(new_price)
            
            print("\nDish updated successfully!")
            break
    
    if not found:
        print("Dish not found!")

def remove_dish():
    print("\n=== Remove Dish ===")
    show_current_menu()
    if len(menu) == 0:
        return
        
    name = input("\nEnter dish name to remove: ")
    
    # Find and remove dish
    for i in range(len(menu)):
        if menu[i][0] == name:
            menu.pop(i)
            print(f"\nDish '{name}' removed successfully!")
            return
    
    print("Dish not found!")

def take_order():
    print("\n=== Take Order ===")
    show_current_menu()
    if len(menu) == 0:
        print("Cannot take order - menu is empty!")
        return
        
    table = input("\nEnter table number: ")
    order_items = []
    
    show_current_menu()
    choice = input("\nEnter dish number (or 'done' to finish): ")
    while choice.lower() != 'done':
        dish_num = int(choice) - 1
        if dish_num >= 0 and dish_num < len(menu):
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                order_items.append([menu[dish_num][0], quantity, menu[dish_num][2]])
        else:
            print("Invalid dish number!")
        
        show_current_menu()
        choice = input("\nEnter dish number (or 'done' to finish): ")
    
    if order_items:
        # Calculate total
        subtotal = 0
        for item in order_items:
            subtotal += item[1] * item[2]
        
        tax = subtotal * 0.10
        total = subtotal + tax
        
        # Store order
        order = [table, order_items, subtotal, tax, total]
        orders.append(order)
        
        # Print bill
        print("\n=== Bill ===")
        print(f"Table: {table}")
        for item in order_items:
            print(f"{item[1]}x {item[0]} - ${item[1] * item[2]:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax (10%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")

def view_reports():
    print("\n=== Reports ===")
    print("1. Sales Report")
    print("2. Inventory Report")
    choice = input("Enter choice (1-2): ")
    
    if choice == "1":
        print("\n=== Sales Report ===")
        total_revenue = 0
        dish_sales = []
        
        # Calculate sales
        for order in orders:
            total_revenue += order[4]
            for item in order[1]:
                found = False
                for dish in dish_sales:
                    if dish[0] == item[0]:
                        dish[1] += item[1]
                        found = True
                        break
                if not found:
                    dish_sales.append([item[0], item[1]])
        
        print(f"Total Revenue: ${total_revenue:.2f}")
        print("\nDish Sales:")
        for dish in dish_sales:
            print(f"{dish[0]}: {dish[1]} orders")
    
    elif choice == "2":
        print("\n=== Inventory Report ===")
        if len(inventory) == 0:
            print("No inventory items found!")
        else:
            for item in inventory:
                print(f"{item[0]}: {item[1]} units")

def main():
    choice = "0"
    while choice != "8":
        print("\n=== Restaurant Management System ===")
        print("1. Add Dish")
        print("2. Update Dish")
        print("3. Remove Dish")
        print("4. Take Order")
        print("5. View Reports")
        print("6. Show Detailed Menu")
        print("7. Show Simple Menu")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "1":
            add_dish()
        elif choice == "2":
            update_dish()
        elif choice == "3":
            remove_dish()
        elif choice == "4":
            take_order()
        elif choice == "5":
            view_reports()
        elif choice == "6":
            show_menu()
        elif choice == "7":
            show_current_menu()
        elif choice == "8":
            print("\nThank you for using the Restaurant Management System!")
        else:
            print("Invalid choice! Please try again.")


main()

