import database
import report 
from tabulate import tabulate
database.create_table()

def show_menu():
    print("******Expense Tracker******")
    print("1.Add expense") 
    print("2.View expense")
    print("3.Update Expense")
    print("4.Delete Expense")
    print("5.Exit")

def add_expense():
    try:
        amount = float(input("Enter The Amount: "))
        category = input("Enter The Category: ")
        description = input("Enter The Description: ")
        date = input("Enter Date (YYYY-MM-DD): ")

        database.insert_expense(amount, category, description, date)
        print("Expense added successfully!")

    except ValueError:
        print("Amount must be a number!")

def view_expense():
    while True:
      print("\n the view expenses menu  options are:\n")
      print("1. View All")
      print("2. filter by category")
      print("3. filter by date rage")
      print("4. show summary/total")
      print("5. Category-wise Summary")
      print("6. Graph Report")
      print("7. exit to main menu")
      
      choice = input("enter your choice:")
      if choice == "1":
         expenses = database.fetch_expenses()
         if not expenses:
             print("No expenses found.")
         else:
             headers = ["ID", "Amount", "Category", "Description", "Date"]
             print(tabulate(expenses, headers=headers, tablefmt="grid"))

      elif choice == "2":
         category = input("Enter category to filter: ")
       
         expenses = database.fetch_expenses_by_category(category)
         if not expenses:
             print("No expenses found for this category.")
         else:
             headers = ["ID", "Amount", "Category", "Description", "Date"]
             print(tabulate(expenses, headers=headers, tablefmt="grid"))

      elif choice == "3":
          start_date = input("Enter the start date (YYYY-MM-DD):")       
          end_date = input("Enter the end date (YYYY-MM-DD):")

          expenses = database.fetch_expenses_by_date(start_date, end_date)

          if not expenses:
             print("No expenses found for this daye range.")
          else:
             headers = ["ID", "Amount", "Category", "Description", "Date"]
             print(tabulate(expenses, headers=headers, tablefmt="grid"))

      elif choice == "4":
         total = database.get_total_expense()
         if total is None:
          print("no expenses to summarize:")
         else:
          print(f"\n total expenses:₹ {total}")
          
      elif choice == "5":
         result_rows = database.get_category_expense()
         if result_rows is None:
          print("no category to summarize:")
         else:
          print("\nCategory-wise Expense Summary:\n")
          for row in result_rows:
            category = row[0]
            total = row[1]
            print(f"{category} : ₹{total}")

      elif choice == "6":
         report.show_category_pie_chart()
         report.show_category_bar_chart()
          
      elif choice == "7":
            print("Returning to Main Menu...")
            break  # now this is VALID

      else:
            print("Invalid choice, try again.")


def update_expense():
    expenses = database.fetch_expenses()
    
    if not expenses:
          print("No expenses found to update.")
          return
    
    headers = ["ID", "Amount", "Category", "Description", "Date"]
    print(tabulate(expenses, headers=headers, tablefmt="grid"))

    expense_id = int(input("Enter Expense Id to update:"))
    new_amount = float(input("Enter New_anount:"))
    new_category = input("Enter New_category:")
    new_description = input("Enter New_description:")
    new_date = input("Enter New_date (YYYY-MM-DD):")
    
    
    database.update_expense(expense_id, new_amount, new_category, new_description, new_date)
    print("Expense updated successfully!")

def delete_expense():
    expenses = database.fetch_expenses()
    
    if not expenses:
          print("No expenses found to update.")
          return

    headers = ["ID", "Amount", "Category", "Description", "Date"]
    print(tabulate(expenses, headers=headers, tablefmt="grid"))

    expense_id = int(input("Enter Expense ID to delete:"))
    confirm = input("Are you sure you want to delete this expense? (y/n): ")
    
    if confirm.lower() == "y":
          database.delete_expense(expense_id)
          print("expense deleted sucessfully")
    else:
          print("Delete Cancelled") 

while True:
    show_menu()
    choice = input("Enter Your Choice:")

    if choice =="1":
        add_expense()
    elif choice =="2":
        view_expense() 

    elif choice == "3":
        update_expense() 

    elif choice=="4":
        delete_expense()

    elif choice =="5":
         print ("EXIT program......")
         break      
        
    else:
        print("invalid choice,please try again....") 