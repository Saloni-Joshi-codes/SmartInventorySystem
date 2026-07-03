import json
from tabulate import tabulate

PURCHASE_FILE = "data/purchases.json"
PRODUCT_FILE = "data/products.json"
SUPPLIER_FILE = "data/suppliers.json"

def load_purchases():
    try:
        with open(PURCHASE_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_purchases(purchases):
    with open(PURCHASE_FILE, "w") as file:
        json.dump(purchases, file, indent=4)

def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_products(products):
    with open(PRODUCT_FILE, "w") as file:
        json.dump(products, file, indent=4)

def load_suppliers():
    try:
        with open(SUPPLIER_FILE, "r") as file:
            return json.load(file)
    except:
        return []
    
def add_purchase():
    purchases = load_purchases()
    products = load_products()
    suppliers = load_suppliers()

    supplier_id = input("Enter Supplier ID: ")

    supplier = None
    for s in suppliers:
        if s["id"] == supplier_id:
            supplier = s
            break

    if not supplier:
        print("Supplier Not Found!")
        return

    product_id = input("Enter Product ID: ")

    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if not product:
        print("Product Not Found!")
        return

    qty = int(input("Enter Quantity Purchased: "))

    total = qty * product["cost_price"]

    purchase = {
        "supplier_id": supplier_id,
        "supplier_name": supplier["company"],
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": qty,
        "total": total
    }

    purchases.append(purchase)
    save_purchases(purchases)

    product["quantity"] += qty
    save_products(products)

    print("Purchase Recorded Successfully!")

def view_purchases():
    purchases = load_purchases()

    if not purchases:
        print("No Purchases Found!")
        return

    table = []

    for p in purchases:
        table.append([
            p["supplier_id"],
            p["supplier_name"],
            p["product_id"],
            p["product_name"],
            p["quantity"],
            p["total"]
        ])

    print(tabulate(
        table,
        headers=["Supplier ID", "Supplier", "Product ID", "Product", "Qty", "Total"],
        tablefmt="grid"
    ))

def purchase_menu():
    while True:
        print("\n========== PURCHASE MANAGEMENT ==========")
        print("1. Add Purchase")
        print("2. View Purchases")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_purchase()
        elif choice == "2":
            view_purchases()
        elif choice == "0":
            break
        else:
            print("Invalid Choice!")