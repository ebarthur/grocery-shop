import tkinter as tk
from tkinter import ttk
import psycopg2

class GroceryStore:
    def __init__(self, root):
        self.root = root
        self.create_table()
        self.create_cart()
        self.create_product_entry()
        self.create_buttons()

    def create_table(self):
        # Create scroll bars
        self.xscroll = ttk.Scrollbar(self.root, orient="horizontal")
        self.yscroll = ttk.Scrollbar(self.root, orient="vertical")

        # Configure style
        style = ttk.Style(self.root)
        style.configure('Treeview', font=(None, 14), rowheight=27)
        style.configure('Treeview.Heading', font=(None, 16))

        # Create record table
        self.table = ttk.Treeview(self.root)

        # Configure scroll bar
        self.xscroll.configure(command=self.table.xview)
        self.yscroll.configure(command=self.table.yview)
        self.table.config(
            yscrollcommand=self.yscroll.set,
            xscrollcommand=self.xscroll.set,
            selectmode="extended",
        )

        # Column configurations
        columns = (
            "Product ID", "Product Name", "Category", "Brand", "Price",
            "Stock Quantity", "Supplier", "Expiry Date", "Discount", "Location",
        )
        self.table["columns"] = columns

        # Add column headings
        for col in columns:
            self.table.heading(col, text=col, anchor=tk.CENTER)

        self.populate_table()

        # Display headings
        self.table["show"] = "headings"

        # Place table and scroll bars to fill the entire window
        self.table.pack(fill="both", expand=True)
        self.xscroll.pack(side="bottom", fill="x")
        self.yscroll.pack(side="right", fill="y")

        # Add search functionality
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(self.root, textvariable=self.search_var)
        search_button = ttk.Button(self.root, text="Search", command=self.search_table)

        search_entry.pack(pady=10)
        search_button.pack()

    def populate_table(self):
        # Create count variable for striped rows
        count = 0

        # Create row stripe tags for alternative row colors
        self.table.tag_configure("oddrow", background="#D9D9D6")
        self.table.tag_configure("evenrow", background="white")

        # Connect to PostgreSQL
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="sigma204"
        )
        
        # Use the connection to execute SQL queries
        with connection.cursor() as cursor:
            # Example query: select all rows from the "inventory" table
            cursor.execute("SELECT * FROM inventory")
            data = cursor.fetchall()

            # Loop through data to add to the table
            for record in data:
                if count % 2 == 0:
                    self.table.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text=count,
                        values=record,
                        tags=("evenrow"),
                    )
                else:
                    self.table.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text=count,
                        values=record,
                        tags=("oddrow"),
                    )
                count += 1

        # Close the database connection
        connection.close()
        
    def search_table(self):
        # Get the search term
        search_term = self.search_var.get().lower()

        # Clear previous search highlights
        for row in self.table.get_children():
            self.table.tag_configure(row, background="white")

        # Highlight rows that match the search term
        for row in self.table.get_children():
            values = self.table.item(row, 'values')
            if any(search_term in str(value).lower() for value in values):
                self.table.tag_configure(row, background="#C0C0C0")  # Highlight in a different color
                
    def create_cart(self):
        self.cart_label = tk.Label(self.root, text="Shopping Cart", font=("Helvetica", 16, "bold"))
        self.cart_label.pack(pady=10)

        self.cart_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=50, height=5)
        self.cart_listbox.pack(pady=10)


    def create_product_entry(self):
        self.product_entry_label = tk.Label(self.root, text="Enter Product ID:")
        self.product_entry_label.pack()

        self.product_entry = ttk.Entry(self.root)
        self.product_entry.pack(pady=5)

    def create_buttons(self):
        self.add_to_cart_button = ttk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack(pady=5)

        self.checkout_button = ttk.Button(self.root, text="Checkout", command=self.checkout)
        self.checkout_button.pack(pady=10)

    def add_to_cart(self):
        product_id = self.product_entry.get()
        if product_id:
            found = False
            for item_id in self.table.get_children():
                values = self.table.item(item_id, 'values')
                if values and values[0] == product_id:
                    found = True
                    product_name = values[1]
                    self.cart_listbox.insert(tk.END, f"{product_name} (ID: {product_id})")
                    self.product_entry.delete(0, tk.END)
                    break

            if not found:
                tk.messagebox.showinfo("Product Not Found", f"No product found with ID: {product_id}")
        else:
            tk.messagebox.showinfo("Empty Product ID", "Please enter a valid product ID.")


    def checkout(self):
        selected_items = self.cart_listbox.get(0, tk.END)
        if selected_items:
            tk.messagebox.showinfo("Checkout", f"Items in Cart:\n{', '.join(selected_items)}\n\nCheckout Successful!")
            self.cart_listbox.delete(0, tk.END)
        else:
            tk.messagebox.showinfo("Empty Cart", "Your cart is empty. Please add items before checking out.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryStore(root)
    root.geometry("1000x500")  # Set the initial size of the window
    root.mainloop()