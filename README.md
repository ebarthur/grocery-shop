
# Tkinter Grocery Application

This is a simple Tkinter application that demonstrates how to create a table using the `ttk.Treeview` widget with scroll bars for displaying production information. The application includes a basic structure with headings and scrollable rows.

## Getting Started

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Prerequisites

This application uses the `tkinter` library, which is included in the Python standard library. No additional dependencies are required.

### Installation

Clone this repository to your local machine:

```bash
git@github.com:ebarthur/tkinter-grocery-app.git
````

Navigate to the project directory:

```bash
cd tkinter-grocery-app
```

Run the application:

```bash
python main.py
```

## Setting Up the Database

1. **Install PostgreSQL:**
   Make sure you have PostgreSQL installed on your machine. You can download it from [PostgreSQL Downloads](https://www.postgresql.org/download/).

2. **Create a Database:**
   Open pgAdmin or any PostgreSQL management tool and create a new database named `grocery_store`. You can use the following SQL command in pgAdmin:

   ```sql
   CREATE DATABASE grocery_store;
   ```

3. **Create a Table:**
   After creating the database, execute the following SQL command to create an `inventory` table within the `grocery_store` database:

   ```sql
   CREATE TABLE inventory (
    product_id VARCHAR(10),
    product_name VARCHAR(255),
    category VARCHAR(50),
    brand VARCHAR(50),
    price VARCHAR(10),
    stock_quantity INTEGER,
    supplier VARCHAR(255),
    expiry_date DATE,
    discount VARCHAR(10),
    location VARCHAR(50)
);
   ```

4. **Insert Sample Data:**
   Optionally, you can insert sample data into the `inventory` table:

   ```sql
   INSERT INTO inventory VALUES
   ('101', 'Banana', 'Fruits', 'Chiquita', '$0.79', 100, 'Local Farms', '2023-01-10', '5%', 'Aisle 1'),
   -- Add more rows as needed
   ```
    ```
    **UPDATE inventory
   SET stock_quantity = 100
   WHERE product_id = '114'::character varying;
   ```
   Please note that the date format should be 'YYYY-MM-DD'.

5. **Update Python Script:**
   Open the `main.py` script and update the PostgreSQL connection details:

   ```python
   # Connect to PostgreSQL
   connection = psycopg2.connect(
       host="localhost",
       database="grocery_store",
       user="your_postgres_user",
       password="your_postgres_password"
   )
   ```

   Replace `your_postgres_user` and `your_postgres_password` with your PostgreSQL username and password.

## Usage

- The application window will open, displaying a table with sample data.
- Customize the `populate_table` method in `main.py` to fetch data from your database using the appropriate method (replace the mock data with actual data).

## Structure

- `main.py`: Contains the main application code, including the `GroceryStore` class that sets up the Tkinter window and the table.
- `commands.py` (not provided): Add your database-related commands and functions here.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

