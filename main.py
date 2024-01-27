'''
I wrote this code to set as foundation for development.
This script is the basic snippet or idea from which I developed
complex and add-on features to implement a fully-functional
Cashier Inventory and Sales Management System in other folders. 
'''

import tkinter as tk
from tkinter import ttk
import psycopg2
import re # not in use

class GroceryStore:
    def __init__(self, root):
        self.root = root
        self.create_table()

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

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryStore(root)
    root.geometry("1000x500")  # Set the initial size of the window
    root.mainloop()
