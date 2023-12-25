
# Tkinter Grocery Application

This is a simple Tkinter application that demonstrates how to create a table using the `ttk.Treeview` widget with scroll bars for displaying production information. The application includes a basic structure with headings and scrollable rows.

## Getting Started

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Prerequisites

This application uses the `tkinter` library, which is included in the Python standard library. No additional dependencies are required.

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/ebarthur/tkinter-gricery-app.git
````

Navigate to the project directory:

```bash
cd tkinter-grocery-app
```

Run the application:

```bash
python main.py
```

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

