import tkinter as tk
from tkinter import ttk, messagebox

# Global variables
menu = []  # List to store menu items
orders = []  # List to store orders

class RestaurantSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("800x600")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create buttons
        self.create_buttons()
        
        # Create menu display area
        self.create_menu_display()
        
    def create_buttons(self):
        # Button frame
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=0, column=0, pady=10)
        
        # Create buttons
        ttk.Button(button_frame, text="Add Dish", command=self.add_dish_window).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Update Dish", command=self.update_dish_window).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Remove Dish", command=self.remove_dish_window).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Take Order", command=self.take_order_window).grid(row=0, column=3, padx=5)
        ttk.Button(button_frame, text="View Reports", command=self.view_reports_window).grid(row=0, column=4, padx=5)
        
    def create_menu_display(self):
        # Menu display frame
        menu_frame = ttk.LabelFrame(self.main_frame, text="Current Menu", padding="10")
        menu_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Create text widget for menu display
        self.menu_text = tk.Text(menu_frame, height=15, width=70)
        self.menu_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(menu_frame, orient=tk.VERTICAL, command=self.menu_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.menu_text['yscrollcommand'] = scrollbar.set
        
        # Update menu display
        self.update_menu_display()
        
    def update_menu_display(self):
        self.menu_text.delete(1.0, tk.END)
        if len(menu) == 0:
            self.menu_text.insert(tk.END, "Menu is empty!")
        else:
            for i in range(len(menu)):
                self.menu_text.insert(tk.END, f"{i+1}. {menu[i][0]}\n")
                self.menu_text.insert(tk.END, f"   Category: {menu[i][1]}\n")
                self.menu_text.insert(tk.END, f"   Price: ${menu[i][2]}\n")
                self.menu_text.insert(tk.END, f"   Ingredients: {', '.join(menu[i][3])}\n\n")
    
    def add_dish_window(self):
        # Create new window
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Dish")
        add_window.geometry("400x300")
        
        # Create input fields
        ttk.Label(add_window, text="Dish Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(add_window, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        category_entry = ttk.Entry(add_window)
        category_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(add_window, text="Price:").grid(row=2, column=0, padx=5, pady=5)
        price_entry = ttk.Entry(add_window)
        price_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(add_window, text="Ingredients:").grid(row=3, column=0, padx=5, pady=5)
        ingredients_text = tk.Text(add_window, height=5, width=30)
        ingredients_text.grid(row=3, column=1, padx=5, pady=5)
        
        def save_dish():
            try:
                name = name_entry.get()
                category = category_entry.get()
                price = float(price_entry.get())
                ingredients = ingredients_text.get(1.0, tk.END).strip().split('\n')
                
                if name and category and price > 0 and ingredients:
                    dish = [name, category, price, ingredients]
                    menu.append(dish)
                    self.update_menu_display()
                    add_window.destroy()
                    messagebox.showinfo("Success", "Dish added successfully!")
                else:
                    messagebox.showerror("Error", "Please fill all fields correctly!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid price!")
        
        ttk.Button(add_window, text="Save", command=save_dish).grid(row=4, column=0, columnspan=2, pady=20)
    
    def update_dish_window(self):
        if len(menu) == 0:
            messagebox.showinfo("Info", "Menu is empty!")
            return
            
        # Create new window
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Dish")
        update_window.geometry("400x300")
        
        # Create dish selection
        ttk.Label(update_window, text="Select Dish:").grid(row=0, column=0, padx=5, pady=5)
        dish_var = tk.StringVar()
        dish_combo = ttk.Combobox(update_window, textvariable=dish_var)
        dish_combo['values'] = [dish[0] for dish in menu]
        dish_combo.grid(row=0, column=1, padx=5, pady=5)
        
        # Create input fields
        ttk.Label(update_window, text="New Name:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(update_window)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(update_window, text="New Category:").grid(row=2, column=0, padx=5, pady=5)
        category_entry = ttk.Entry(update_window)
        category_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(update_window, text="New Price:").grid(row=3, column=0, padx=5, pady=5)
        price_entry = ttk.Entry(update_window)
        price_entry.grid(row=3, column=1, padx=5, pady=5)
        
        def update_dish():
            try:
                selected_dish = dish_var.get()
                for i in range(len(menu)):
                    if menu[i][0] == selected_dish:
                        new_name = name_entry.get()
                        new_category = category_entry.get()
                        new_price = price_entry.get()
                        
                        if new_name:
                            menu[i][0] = new_name
                        if new_category:
                            menu[i][1] = new_category
                        if new_price:
                            menu[i][2] = float(new_price)
                        
                        self.update_menu_display()
                        update_window.destroy()
                        messagebox.showinfo("Success", "Dish updated successfully!")
                        return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid price!")
        
        ttk.Button(update_window, text="Update", command=update_dish).grid(row=4, column=0, columnspan=2, pady=20)
    
    def remove_dish_window(self):
        if len(menu) == 0:
            messagebox.showinfo("Info", "Menu is empty!")
            return
            
        # Create new window
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Dish")
        remove_window.geometry("300x150")
        
        # Create dish selection
        ttk.Label(remove_window, text="Select Dish to Remove:").grid(row=0, column=0, padx=5, pady=5)
        dish_var = tk.StringVar()
        dish_combo = ttk.Combobox(remove_window, textvariable=dish_var)
        dish_combo['values'] = [dish[0] for dish in menu]
        dish_combo.grid(row=0, column=1, padx=5, pady=5)
        
        def remove_dish():
            selected_dish = dish_var.get()
            for i in range(len(menu)):
                if menu[i][0] == selected_dish:
                    menu.pop(i)
                    self.update_menu_display()
                    remove_window.destroy()
                    messagebox.showinfo("Success", "Dish removed successfully!")
                    return
        
        ttk.Button(remove_window, text="Remove", command=remove_dish).grid(row=1, column=0, columnspan=2, pady=20)
    
    def take_order_window(self):
        if len(menu) == 0:
            messagebox.showinfo("Info", "Menu is empty!")
            return
            
        # Create new window
        order_window = tk.Toplevel(self.root)
        order_window.title("Take Order")
        order_window.geometry("500x400")
        
        # Create order items list
        order_items = []
        
        # Create table number input
        ttk.Label(order_window, text="Table Number:").grid(row=0, column=0, padx=5, pady=5)
        table_entry = ttk.Entry(order_window)
        table_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Create dish selection
        ttk.Label(order_window, text="Select Dish:").grid(row=1, column=0, padx=5, pady=5)
        dish_var = tk.StringVar()
        dish_combo = ttk.Combobox(order_window, textvariable=dish_var)
        dish_combo['values'] = [dish[0] for dish in menu]
        dish_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Create quantity input
        ttk.Label(order_window, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        quantity_entry = ttk.Entry(order_window)
        quantity_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Create order display
        order_text = tk.Text(order_window, height=10, width=50)
        order_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        def add_to_order():
            try:
                dish_name = dish_var.get()
                quantity = int(quantity_entry.get())
                
                if quantity > 0:
                    for dish in menu:
                        if dish[0] == dish_name:
                            order_items.append([dish_name, quantity, dish[2]])
                            order_text.insert(tk.END, f"{quantity}x {dish_name} - ${quantity * dish[2]:.2f}\n")
                            break
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid quantity!")
        
        def save_order():
            if not order_items:
                messagebox.showerror("Error", "No items in order!")
                return
                
            table = table_entry.get()
            if not table:
                messagebox.showerror("Error", "Please enter table number!")
                return
            
            # Calculate total
            subtotal = sum(item[1] * item[2] for item in order_items)
            tax = subtotal * 0.10
            total = subtotal + tax
            
            # Store order
            order = [table, order_items, subtotal, tax, total]
            orders.append(order)
            
            # Show bill
            bill_window = tk.Toplevel(order_window)
            bill_window.title("Bill")
            bill_window.geometry("300x400")
            
            bill_text = tk.Text(bill_window, height=20, width=35)
            bill_text.grid(row=0, column=0, padx=5, pady=5)
            
            bill_text.insert(tk.END, f"Table: {table}\n\n")
            for item in order_items:
                bill_text.insert(tk.END, f"{item[1]}x {item[0]} - ${item[1] * item[2]:.2f}\n")
            bill_text.insert(tk.END, f"\nSubtotal: ${subtotal:.2f}\n")
            bill_text.insert(tk.END, f"Tax (10%): ${tax:.2f}\n")
            bill_text.insert(tk.END, f"Total: ${total:.2f}\n")
            
            order_window.destroy()
        
        ttk.Button(order_window, text="Add to Order", command=add_to_order).grid(row=4, column=0, pady=10)
        ttk.Button(order_window, text="Save Order", command=save_order).grid(row=4, column=1, pady=10)
    
    def view_reports_window(self):
        if len(orders) == 0:
            messagebox.showinfo("Info", "No orders to display!")
            return
            
        # Create new window
        reports_window = tk.Toplevel(self.root)
        reports_window.title("Reports")
        reports_window.geometry("400x500")
        
        # Create report display
        report_text = tk.Text(reports_window, height=25, width=45)
        report_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Calculate total revenue
        total_revenue = sum(order[4] for order in orders)
        report_text.insert(tk.END, f"Total Revenue: ${total_revenue:.2f}\n\n")
        
        # Calculate dish sales
        dish_sales = []
        for order in orders:
            for item in order[1]:
                found = False
                for dish in dish_sales:
                    if dish[0] == item[0]:
                        dish[1] += item[1]
                        found = True
                        break
                if not found:
                    dish_sales.append([item[0], item[1]])
        
        report_text.insert(tk.END, "Dish Sales:\n")
        for dish in dish_sales:
            report_text.insert(tk.END, f"{dish[0]}: {dish[1]} orders\n")

def main():
    root = tk.Tk()
    app = RestaurantSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()