import json
import os
from tabulate import tabulate

FILE_PATH = "data/products.json"

# Create file if it doesn't exist
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump([], file)


def load_products():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_products(products):
    with open(FILE_PATH, "w") as file:
        json.dump(products, file, indent=4)


def add_product():
    products = load_products()

    print("\n===== Add Product =====")

    product = {
        "id": input("Product ID: "),
        "name": input("Product Name: "),
        "category": input("Category: "),
        "cost_price": float(input("Cost Price: ")),
        "selling_price": float(input("Selling Price: ")),
        "quantity": int(input("Quantity: ")),
        "supplier": input("Supplier: ")
    }

    products.append(product)
    save_products(products)

    print("\n✅ Product Added Successfully!")


def view_products():
    products = load_products()

    if not products:
        print("\nNo Products Found.")
        return

    table = []

    for p in products:
        table.append([
            p["id"],
            p["name"],
            p["category"],
            p["cost_price"],
            p["selling_price"],
            p["quantity"],
            p["supplier"]
        ])

    print()
    print(tabulate(
        table,
        headers=[
            "ID",
            "Name",
            "Category",
            "Cost",
            "Selling",
            "Stock",
            "Supplier"
        ],
        tablefmt="grid"
    ))

def search_product():
    products = load_products()

    search = input("\nEnter Product ID or Name: ").lower()

    found = False

    for p in products:
        if p["id"].lower() == search or p["name"].lower() == search:
            print("\nProduct Found")
            print("---------------------------")
            print(f"ID            : {p['id']}")
            print(f"Name          : {p['name']}")
            print(f"Category      : {p['category']}")
            print(f"Cost Price    : {p['cost_price']}")
            print(f"Selling Price : {p['selling_price']}")
            print(f"Quantity      : {p['quantity']}")
            print(f"Supplier      : {p['supplier']}")
            found = True
            break

    if not found:
        print("\n❌ Product Not Found!")
        
def update_product():
    products = load_products()

    product_id = input("\nEnter Product ID to Update: ")

    for product in products:
        if product["id"] == product_id:

            print("\nLeave blank to keep the old value.\n")

            name = input(f"Product Name ({product['name']}): ")
            category = input(f"Category ({product['category']}): ")
            cost = input(f"Cost Price ({product['cost_price']}): ")
            selling = input(f"Selling Price ({product['selling_price']}): ")
            quantity = input(f"Quantity ({product['quantity']}): ")
            supplier = input(f"Supplier ({product['supplier']}): ")

            if name:
                product["name"] = name
            if category:
                product["category"] = category
            if cost:
                product["cost_price"] = float(cost)
            if selling:
                product["selling_price"] = float(selling)
            if quantity:
                product["quantity"] = int(quantity)
            if supplier:
                product["supplier"] = supplier

            save_products(products)

            print("\n✅ Product Updated Successfully!")
            return

    print("\n❌ Product Not Found!")

def delete_product():
    products = load_products()

    product_id = input("\nEnter Product ID to Delete: ")

    for product in products:
        if product["id"] == product_id:

            confirm = input(f"Delete {product['name']}? (y/n): ")

            if confirm.lower() == "y":
                products.remove(product)
                save_products(products)
                print("\n✅ Product Deleted Successfully!")
            else:
                print("\nDeletion Cancelled.")

            return

    print("\n❌ Product Not Found!")

def product_menu():
    while True:

        print("\n========== PRODUCT MANAGEMENT ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")