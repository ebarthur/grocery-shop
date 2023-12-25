
# Cashier Application README

## Overview

This Cashier Application is a simple point-of-sale system that allows cashiers to interact with a graphical user interface to add products to a cart and proceed to checkout. The application is built using the Tkinter library for the graphical interface and connects to a PostgreSQL database to retrieve product information.

## Features

- **Product Display:** The application displays a table of products retrieved from a PostgreSQL database. Products are categorized by columns such as Product ID, Product Name, Category, Brand, Price, Stock Quantity, Supplier, Expiry Date, Discount, and Location.

- **Search Functionality:** Cashiers can search for products by entering keywords in a search box. The application highlights the rows that match the search term for easy identification.

- **Adding to Cart:** Cashiers can input the Product ID of a desired product in the provided entry field. Upon clicking the "Add to Cart" button, the selected product is added to a shopping cart displayed on the interface.

- **Checkout:** The "Checkout" button completes the transaction by displaying a messagebox with a summary of the items in the shopping cart. The cart is then cleared for the next transaction.

## Usage

1. **Database Configuration:**
   - Ensure that you have a PostgreSQL database with a table named "inventory" containing columns for Product ID, Product Name, Category, Brand, Price, Stock Quantity, Supplier, Expiry Date, Discount, and Location.

2. **Dependencies:**
   - Install the required dependencies by running:
     ```bash
     pip install psycopg2
     ```

3. **Run the Application:**
   - Execute the script by running:
     ```bash
     python cashier_app.py
     ```

4. **Interacting with the Application:**
   - Use the search box to find specific products.
   - Input the Product ID to add products to the cart.
   - Click the "Checkout" button to complete the transaction.

## Contributing

Contributions to this Cashier Application are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This Cashier Application is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

