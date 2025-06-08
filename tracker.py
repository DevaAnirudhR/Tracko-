import csv
import sys
from datetime import datetime

filename = "expenses.csv"

def add_expense(amount, category):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), amount, category])
    print(f"Added: {amount} - {category}")

def list_expenses():
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            print("\n📋 Expenses:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found.")

def total_expenses():
    try:
        total = 0
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"\n Total Spent: {total}")
    except FileNotFoundError:
        print(" No data yet.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add <amount> <category> | list | total")
    elif sys.argv[1] == "add":
        add_expense(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "list":
        list_expenses()
    elif sys.argv[1] == "total":
        total_expenses()
    else:
        print("Unknown command")
        
