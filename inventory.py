import json

FILE_PATH = "data/products.json"


def load_products():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_products(products):
    with open(FILE_PATH, "w") as file:
        json.dump(products, file, indent=4)


def view_stock():
    products = load_products()

    if not products:
        print("\nNo Products Available!")
        return

    print("\n========== CURRENT STOCK ==========\n")

    for p in products:
        print(f"ID       : {p['id']}")
        print(f"Product  : {p['name']}")
        print(f"Stock    : {p['quantity']}")
        print("-" * 30)


def restock_product():
    products = load_products()

    pid = input("Enter Product ID: ")

    for p in products:
        if p["id"] == pid:
            qty = int(input("Enter Quantity to Add: "))
            p["quantity"] += qty
            save_products(products)

            print("\n✅ Stock Updated Successfully!")
            return

    print("\n❌ Product Not Found!")


def low_stock():
    products = load_products()

    print("\n======= LOW STOCK PRODUCTS =======")

    found = False

    for p in products:
        if p["quantity"] < 5:
            found = True
            print(f"{p['name']} --> {p['quantity']}")

    if not found:
        print("No Low Stock Products.")


def inventory_menu():

    while True:

        print("\n========== INVENTORY MANAGEMENT ==========")
        print("1. View Current Stock")
        print("2. Restock Product")
        print("3. Reduce Stock (Coming Soon)")
        print("4. Low Stock Alert")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            view_stock()

        elif choice == "2":
            restock_product()

        elif choice == "3":
            print("Coming Soon...")

        elif choice == "4":
            low_stock()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")