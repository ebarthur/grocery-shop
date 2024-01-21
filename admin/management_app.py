import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.simpledialog
import psycopg2
import re
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GroceryStoreManager:
    def __init__(self, root):
        self.root = root
        self.create_manager_interface()
        self.connect_to_database()
        self.app = app

    def connect_to_database(self):
        # Modify the connection parameters based on your PostgreSQL setup
        self.connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="sigma204"
        )
        
    def create_manager_interface(self):
        manager_frame = ttk.LabelFrame(self.root, text="Manager Interface")
        manager_frame.pack(pady=10)

        update_inventory_button = ttk.Button(manager_frame, text="Update Inventory", command=self.update_inventory)
        update_inventory_button.grid(row=0, column=0, padx=5)

        generate_sales_graph_button = ttk.Button(manager_frame, text="Generate Sales Graph", command=self.generate_sales_graph)
        generate_sales_graph_button.grid(row=0, column=1, padx=5)

        add_product_button = ttk.Button(manager_frame, text="Add New Product", command=self.add_new_product)
        add_product_button.grid(row=0, column=2, padx=5)

        remove_expired_button = ttk.Button(manager_frame, text="Remove Expired Products", command=self.remove_expired_products)
        remove_expired_button.grid(row=0, column=3, padx=5)

    def update_inventory(self):
        # Create a dialog to get product ID
        product_id = tkinter.simpledialog.askstring("Update Inventory", "Enter Product ID:")

        # Check if the product ID is provided
        if product_id:
            # Check if the product ID exists in the database
            if self.check_product_exists(product_id):
                # Fetch existing data from the database
                existing_data = self.get_product_data(product_id)

                # Create a new window for updating inventory
                update_window = tk.Toplevel(self.root)
                update_window.title("Update Inventory")

                # Create labels and entry widgets for each column
                labels = ["Product Name", "Category", "Brand", "Price", "Stock Quantity",
                          "Supplier", "Expiry Date", "Discount", "Location"]

                entry_vars = []
                entry_widgets = []

                for i, (label_text, existing_value) in enumerate(zip(labels, existing_data)):
                    label = ttk.Label(update_window, text=label_text + ":")
                    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)

                    entry_var = tk.StringVar(value=existing_value)
                    entry = ttk.Entry(update_window, textvariable=entry_var)
                    entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)

                    entry_vars.append(entry_var)
                    entry_widgets.append(entry)
                    
                # Function to perform the update
                def perform_update():
                    # Get values from entry widgets
                    updated_values = [entry_var.get() for entry_var in entry_vars]

                    # Update the inventory in the database
                    self.perform_update(product_id, updated_values, update_window)

                # Add a button to perform the update
                update_button = ttk.Button(update_window, text="Update", command=perform_update)
                update_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

            else:
                tk.messagebox.showinfo("Product Not Found", f"No product found with ID: {product_id}")

        else:
            tk.messagebox.showinfo("Empty Product ID", "Please enter a valid product ID.")

    def check_product_exists(self, product_id):
        # Check if the product ID exists in the "inventory" table
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM inventory WHERE product_id = %s", (product_id,))
            return cursor.fetchone() is not None

    def get_product_data(self, product_id):
        # Fetch data from the "inventory" table where "Product ID" matches
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT product_name, category, brand, price, stock_quantity, "
                           "supplier, expiry_date, discount, location "
                           "FROM inventory WHERE product_id = %s", (product_id,))
            return cursor.fetchone()
        
    def perform_update(self, product_id, values, update_window):
        # Update the inventory in the "inventory" table where "Product ID" matches
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE inventory SET product_name = %s, category = %s, "
                            "brand = %s, price = %s, stock_quantity = %s, "
                            "supplier = %s, expiry_date = %s, discount = %s, location = %s "
                            "WHERE product_id = %s",
                            (values[0], values[1], values[2], values[3], values[4],
                             values[5], values[6], values[7], values[8], product_id))

            # Commit the changes to the database
            self.connection.commit()

        # Display a success message
        tk.messagebox.showinfo("Update Inventory", "Inventory updated successfully.")

        # Close the update window
        update_window.destroy()

        # Refresh the table to reflect the updated data
        self.populate_table()
        
    def generate_sales_graph(self):
            # I are working on sales data
            tk.messagebox.showinfo("Sales Data in Progress", "We are currently working on Sales data. Please come back another time.")
            
    def add_new_product(self):
        # Create a new window for adding a new product
        add_product_window = tk.Toplevel(self.root)
        add_product_window.title("Add New Product")

        # Create labels and entry widgets for each column, including "Product ID"
        labels = ["Product ID", "Product Name", "Category", "Brand", "Price", "Stock Quantity",
                "Supplier", "Expiry Date", "Discount", "Location"]

        entry_vars = []
        entry_widgets = []

        for i, label_text in enumerate(labels):
            label = ttk.Label(add_product_window, text=label_text + ":")
            label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)

            entry_var = tk.StringVar()
            entry = ttk.Entry(add_product_window, textvariable=entry_var)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)

            entry_vars.append(entry_var)
            entry_widgets.append(entry)

        # Function to perform the addition of a new product
        def perform_addition():
            # Get values from entry widgets
            new_product_values = [entry_var.get() for entry_var in entry_vars]

            # Add the new product to the inventory in the database
            self.perform_addition(new_product_values, add_product_window)

        # Add a button to perform the addition
        add_button = ttk.Button(add_product_window, text="Add Product", command=perform_addition)
        add_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

    def perform_addition(self, values, add_product_window):
        # Check if the product ID already exists in the "inventory" table
        if self.check_product_exists(values[0]):
            tk.messagebox.showinfo("Product ID Exists", f"Product ID {values[0]} already exists. Please use a unique ID.")
        else:
            # Insert the new product into the "inventory" table
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO inventory (product_id, product_name, category, brand, price, stock_quantity, "
                            "supplier, expiry_date, discount, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (values[0], values[1], values[2], values[3], values[4],
                                values[5], values[6], values[7], values[8], values[9]))

                # Commit the changes to the database
                self.connection.commit()

            # Display a success message
            tk.messagebox.showinfo("Add New Product", "New product added successfully.")

            # Close the add product window
            add_product_window.destroy()

            # Refresh the table to reflect the updated data
            self.populate_table()

    def check_product_exists(self, product_id):
        # Check if the product ID exists in the "inventory" table
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM inventory WHERE product_id = %s", (product_id,))
            return cursor.fetchone() is not None
    
    def remove_expired_products(self):
        # I am also working on sales data
            tk.messagebox.showinfo("Remove Expired Products in Progress", "We are currently working on Removing Expired products. Please come back another time.")

class GroceryStoreApp:
    def __init__(self, root):
        self.root = root
        self.create_table()
        self.create_cart()
        self.create_product_entry()
        self.create_buttons()

    def create_table(self):
        # Implement create_table method here
        # This could include creating a Treeview widget and configuring columns
        # Populate the table
        pass

    def create_cart(self):
        # Implement create_cart method here
        pass

    def create_product_entry(self):
        # Implement create_product_entry method here
        pass

    def create_buttons(self):
        # Implement create_buttons method here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryStoreApp(root)
    manager_interface = GroceryStoreManager(root)
    root.geometry("1000x500")
    root.mainloop()
