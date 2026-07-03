import json
import os
from tabulate import tabulate

FILE_PATH = "data/suppliers.json"

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump([], file)


def load_suppliers():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_suppliers(suppliers):
    with open(FILE_PATH, "w") as file:
        json.dump(suppliers, file, indent=4)


def add_supplier():
    suppliers = load_suppliers()

    supplier = {
        "id": input("Supplier ID: "),
        "company": input("Company Name: "),
        "phone": input("Phone: "),
        "email": input("Email: "),
        "address": input("Address: ")
    }

    suppliers.append(supplier)
    save_suppliers(suppliers)

    print("\n✅ Supplier Added Successfully!")


def view_suppliers():
    suppliers = load_suppliers()

    if not suppliers:
        print("\nNo Suppliers Found!")
        return

    table = []

    for s in suppliers:
        table.append([
            s["id"],
            s["company"],
            s["phone"],
            s["email"],
            s["address"]
        ])

    print(tabulate(
        table,
        headers=["ID", "Company", "Phone", "Email", "Address"],
        tablefmt="grid"
    ))


def search_supplier():
    suppliers = load_suppliers()

    sid = input("Enter Supplier ID: ")

    for s in suppliers:
        if s["id"] == sid:
            print("\nSupplier Found")
            print("-------------------------")
            print("ID:", s["id"])
            print("Company:", s["company"])
            print("Phone:", s["phone"])
            print("Email:", s["email"])
            print("Address:", s["address"])
            return

    print("\nSupplier Not Found!")


def delete_supplier():
    suppliers = load_suppliers()

    sid = input("Enter Supplier ID: ")

    for s in suppliers:
        if s["id"] == sid:

            confirm = input("Delete this supplier? (y/n): ")

            if confirm.lower() == "y":
                suppliers.remove(s)
                save_suppliers(suppliers)
                print("\n✅ Supplier Deleted Successfully!")

            return

    print("\nSupplier Not Found!")


def supplier_menu():

    while True:

        print("\n========== SUPPLIER MANAGEMENT ==========")
        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Search Supplier")
        print("4. Delete Supplier")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_supplier()

        elif choice == "2":
            view_suppliers()

        elif choice == "3":
            search_supplier()

        elif choice == "4":
            delete_supplier()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")