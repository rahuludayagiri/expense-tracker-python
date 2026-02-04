import sqlite3
def connect_db():
    return sqlite3.connect("expenses.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    date REAL NOT NULL
)
""")
    conn.commit()
    conn.close()

def insert_expense(amount,category,description,date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
          INSERT INTO expenses(amount, category, description, date)
          VALUES (?, ?, ?, ?)
      """,(amount, category, description, date))
    conn.commit()
    conn.close()

def fetch_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()

    conn.close()
    return records

def fetch_expenses_by_category(category):
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM expenses WHERE category = ?",
        (category,)
    )

    results = cursor.fetchall()
    conn.close()
    return results


def fetch_expenses_by_date(start_date, end_date):
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute("""
       SELECT * FROM expenses
       WHERE date BETWEEN ? AND ?
    """, (start_date, end_date))             

    results = cursor.fetchall()
    conn.close()
    return results

def get_total_expense():
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute("select sum(amount) from expenses")
    total = cursor.fetchone()[0]
    
    conn.close()
    return total

def get_category_expense():
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute("""
        select category,sum(amount)
        from expenses
        GROUP BY category
    """)
    result_rows = cursor.fetchall()
    
    conn.close()
    return result_rows

def update_expense(id, new_amount, new_category, new_description, new_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
          update expenses
          set amount = ?, category = ?, description = ?, date = ?
          where id = ?
       """,(new_amount, new_category, new_description, new_date, id))
    conn.commit()
    conn.close()

def delete_expense(id):
   conn = connect_db()
   cursor = conn.cursor() 
   cursor.execute("""
         delete from expenses where id = ?
       """, (id,))
   conn.commit()
   conn.close()  
