import json
import os
from tabulate import tabulate

FILE_PATH = "data/customers.json"

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump([], file)


def load_customers():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_customers(customers):
    with open(FILE_PATH, "w") as file:
        json.dump(customers, file, indent=4)


def add_customer():
    customers = load_customers()

    customer = {
        "id": input("Customer ID: "),
        "name": input("Customer Name: "),
        "phone": input("Phone: "),
        "email": input("Email: ")
    }

    customers.append(customer)
    save_customers(customers)

    print("\n✅ Customer Added Successfully!")


def view_customers():
    customers = load_customers()

    if not customers:
        print("\nNo Customers Found!")
        return

    table = []

    for c in customers:
        table.append([
            c["id"],
            c["name"],
            c["phone"],
            c["email"]
        ])

    print(tabulate(
        table,
        headers=["ID", "Name", "Phone", "Email"],
        tablefmt="grid"
    ))


def search_customer():
    customers = load_customers()

    cid = input("Enter Customer ID: ")

    for c in customers:
        if c["id"] == cid:
            print("\nCustomer Found")
            print("-----------------------")
            print("ID:", c["id"])
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            return

    print("\nCustomer Not Found!")


def delete_customer():
    customers = load_customers()

    cid = input("Enter Customer ID: ")

    for c in customers:
        if c["id"] == cid:

            confirm = input("Delete this customer? (y/n): ")

            if confirm.lower() == "y":
                customers.remove(c)
                save_customers(customers)
                print("\n✅ Customer Deleted Successfully!")

            return

    print("\nCustomer Not Found!")


def customer_menu():

    while True:

        print("\n========== CUSTOMER MANAGEMENT ==========")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Delete Customer")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            delete_customer()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")