import matplotlib.pyplot as plt
import database

def show_category_pie_chart():
    data = database.get_category_expense()

    if not data:
        print("No Data to Plot")
        return

    categories = []
    totals = []

    for category, total in data:
        categories.append(category)
        totals.append(total)

    plt.figure()
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Category-wise Expense Distribution")
    plt.show()

def show_category_bar_chart():
    data = database.get_category_expense()
    
    if not data:
        print("No Data to Plot")
        return

    categories = []
    totals = []

    for category, total in data:
        categories.append(category)
        totals.append(total)

    plt.bar(categories, totals)
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.title("Category vs Total Expenses")
    plt.show()