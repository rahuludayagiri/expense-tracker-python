# Expense Tracker (Python)

## Overview
This is a console-based Expense Tracker application developed using Python and SQLite.  
The application allows users to add, view, update, delete, filter, and analyze their expenses.  
It also provides category-wise summaries and graphical reports for better expense visualization.

## Features
- Add new expenses with amount, category, description, and date
- View all expenses in a tabular format
- Filter expenses by category
- Filter expenses by date range
- Update existing expenses
- Delete expenses
- View total expense summary
- View category-wise expense summary
- Generate graphical reports (Pie chart and Bar chart)

## Technologies Used
- Python 3
- SQLite3 (Database)
- SQL (CRUD operations, filtering, aggregation)
- Tabulate (for table display)
- Matplotlib (for graphical reports)

## Project Structure

Expense-Tracker/
│
├── main.py        # Handles user interaction and application flow
├── database.py    # Contains all database-related operations
├── report.py      # Generates graphical reports
├── expenses.db    # SQLite database file
└── README.md      # Project documentation

## How to Run the Project

1. Make sure Python 3 is installed on your system
2. Clone the repository or download the project files
3. Install required dependencies:
   ```bash
   pip install tabulate matplotlib
````

4. Run the application:

   ```bash
   python main.py
   ## 🧠 What you should understand here (important)
- `pip install` → installs external libraries you used
- `python main.py` → entry point of your project
- Anyone can now run your app without asking you

This shows **ownership** of your project.

---

### ✅ Stop here again
Save the file.
   ```

```

---

## Future Enhancements

- Add user authentication
- Export expenses to CSV or Excel
- Convert the console application into a web application
- Add monthly and yearly expense analysis
- Improve error handling and input validation

