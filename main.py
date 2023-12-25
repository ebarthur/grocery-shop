import tkinter as tk
from tkinter import ttk

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

        # Mock data for a grocery store (replace with your actual data)
        data = [
            ("101", "Banana", "Fruits", "Chiquita", "$0.79", "100", "Local Farms", "2023-01-10", "5%", "Aisle 1"),
            ("102", "Milk", "Dairy", "Organic Farms", "$2.50", "50", "DairyCo", "2023-01-15", "0%", "Refrigerated Section"),
            ("103", "Bread", "Bakery", "Wonder Bread", "$1.99", "75", "Bakery Delights", "2023-01-12", "10%", "Aisle 3"),
            ("104", "Eggs", "Dairy", "Farm Fresh", "$1.25", "120", "Eggcellent Farms", "2023-01-20", "8%", "Refrigerated Section"),
            ("105", "Cereal", "Breakfast", "Kellogg's", "$3.49", "30", "Cereal Haven", "2023-02-01", "15%", "Aisle 2"),
            ("106", "Tomato", "Vegetables", "Sunshine Farms", "$0.99", "80", "Local Farms", "2023-01-08", "0%", "Produce Section"),
            ("107", "Chicken", "Meat", "Tyson", "$4.99", "40", "Meat Masters", "2023-01-18", "12%", "Meat Department"),
            ("108", "Yogurt", "Dairy", "Yoplait", "$1.75", "60", "DairyCo", "2023-01-25", "5%", "Refrigerated Section"),
            ("109", "Pasta", "Pantry", "Barilla", "$1.49", "90", "Pasta Paradise", "2023-01-14", "10%", "Aisle 4"),
            ("110", "Apples", "Fruits", "Washington Apples", "$1.29", "70", "Local Farms", "2023-01-09", "3%", "Produce Section"),
            ("111", "Orange Juice", "Beverages", "Tropicana", "$2.99", "40", "Juice Co.", "2023-01-25", "0%", "Beverage Section"),
            ("112", "Potatoes", "Vegetables", "Idaho Potatoes", "$0.89", "60", "Local Farms", "2023-01-15", "2%", "Produce Section"),
            ("113", "Cheese", "Dairy", "Kraft", "$3.29", "25", "DairyCo", "2023-01-30", "5%", "Refrigerated Section"),
            ("114", "Salmon", "Seafood", "Wild Catch", "$9.99", "15", "Seafood Delights", "2023-02-05", "20%", "Seafood Department"),
            ("115", "Pineapple", "Fruits", "Dole", "$1.99", "30", "Fruit Haven", "2023-01-12", "0%", "Produce Section"),
            ("116", "Toothpaste", "Personal Care", "Colgate", "$2.49", "50", "Personal Care Co.", "2023-01-28", "0%", "Health and Beauty Section"),
            ("117", "Ice Cream", "Frozen", "Ben & Jerry's", "$4.99", "20", "Frozen Delights", "2023-02-10", "15%", "Frozen Foods Section"),
            ("118", "Shampoo", "Personal Care", "Pantene", "$3.99", "40", "Personal Care Co.", "2023-01-22", "8%", "Health and Beauty Section"),
            ("119", "Ground Beef", "Meat", "Angus Farms", "$5.49", "35", "Meat Masters", "2023-01-15", "10%", "Meat Department"),
            ("120", "Lettuce", "Vegetables", "Fresh Farms", "$1.49", "40", "Local Farms", "2023-01-18", "0%", "Produce Section"),
            ("121", "Peanut Butter", "Pantry", "Skippy", "$2.99", "25", "Pantry Essentials", "2023-02-15", "5%", "Aisle 5"),
            ("122", "Almond Milk", "Dairy", "Silk", "$3.50", "30", "DairyCo", "2023-02-28", "0%", "Refrigerated Section"),
            ("123", "Carrots", "Vegetables", "Bunny Farms", "$0.99", "50", "Local Farms", "2023-02-10", "3%", "Produce Section"),
            ("124", "Pizza", "Frozen", "DiGiorno", "$5.99", "15", "Frozen Delights", "2023-02-18", "10%", "Frozen Foods Section"),
            ("125", "Mango", "Fruits", "MangoWorld", "$1.49", "40", "Fruit Haven", "2023-02-05", "0%", "Produce Section"),
            ("126", "Soap", "Personal Care", "Dove", "$1.99", "60", "Personal Care Co.", "2023-02-20", "5%", "Health and Beauty Section"),
            ("127", "Fish Sticks", "Seafood", "Gorton's", "$4.25", "20", "Seafood Delights", "2023-02-15", "8%", "Seafood Department"),
            ("128", "Rice", "Pantry", "Uncle Ben's", "$2.49", "50", "Pantry Essentials", "2023-02-10", "0%", "Aisle 6"),
            ("129", "Orange", "Fruits", "Sunkist", "$0.75", "60", "Local Farms", "2023-02-12", "2%", "Produce Section"),
            ("130", "Conditioner", "Personal Care", "Herbal Essences", "$3.99", "35", "Personal Care Co.", "2023-02-25", "5%", "Health and Beauty Section"),
            # Add more rows as needed
        ]

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
