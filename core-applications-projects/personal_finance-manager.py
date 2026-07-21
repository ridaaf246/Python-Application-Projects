import json
import os

file_name = "finance_data.json"


def load_data():
    if os.path.exists(file_name):
        try:
            file = open(file_name, "r")
            data = json.load(file)
            file.close()
            return data

        except:
            print("File error")
            return []

    else:
        return []


def save_data(data):
    try:
        file = open(file_name, "w")
        json.dump(data, file, indent=4)
        file.close()

    except:
        print("Data save error")


def add_transaction(data):
    try:
        title = input("Enter title: ")
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        typ = input("Enter type (Income/Expense): ")

        record = {
            "title": title,
            "amount": amount,
            "category": category,
            "type": typ
        }

        data.append(record)

        save_data(data)

        print("Transaction added successfully")

    except:
        print("Enter amount in numbers")


def show_transactions(data):
    if len(data) == 0:
        print("No transactions found")

    else:
        for i in range(len(data)):
            print("\nTransaction", i + 1)
            print("Title:", data[i]["title"])
            print("Amount:", data[i]["amount"])
            print("Category:", data[i]["category"])
            print("Type:", data[i]["type"])


def calculate_balance(data):
    income = 0
    expense = 0

    for item in data:
        if item["type"].lower() == "income":
            income += item["amount"]

        else:
            expense += item["amount"]

    print("Total Income:", income)
    print("Total Expense:", expense)
    print("Current Balance:", income - expense)


def search_transaction(data):
    title = input("Enter title to search: ")

    found = False

    for item in data:
        if item["title"].lower() == title.lower():
            print("Transaction Found")
            print("Title:", item["title"])
            print("Amount:", item["amount"])
            print("Category:", item["category"])
            print("Type:", item["type"])

            found = True

    if found == False:
        print("Transaction not found")


def delete_transaction(data):
    try:
        show_transactions(data)

        num = int(input("Enter transaction number: "))

        data.pop(num - 1)

        save_data(data)

        print("Transaction deleted")

    except:
        print("Invalid choice")


transactions = load_data()


while True:
    print("Personal Finance Manager")
    print("1. Add Transaction")
    print("2. Show Transactions")
    print("3. Calculate Balance")
    print("4. Search Transaction")
    print("5. Delete Transaction")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_transaction(transactions)

    elif choice == "2":
        show_transactions(transactions)

    elif choice == "3":
        calculate_balance(transactions)

    elif choice == "4":
        search_transaction(transactions)

    elif choice == "5":
        delete_transaction(transactions)

    elif choice == "6":
        print("Program closed")
        break

    else:
        print("Wrong choice")