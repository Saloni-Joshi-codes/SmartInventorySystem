import json
from tabulate import tabulate

SALES_FILE = "data/sales.json"
PRODUCT_FILE = "data/products.json"
CUSTOMER_FILE = "data/customers.json"


def load_sales():
    try:
        with open(SALES_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_sales(sales):
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=4)


def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_products(products):
    with open(PRODUCT_FILE, "w") as file:
        json.dump(products, file, indent=4)


def load_customers():
    try:
        with open(CUSTOMER_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def add_sale():
    sales = load_sales()
    products = load_products()
    customers = load_customers()

    customer_id = input("Enter Customer ID: ")

    customer = None
    for c in customers:
        if c["id"] == customer_id:
            customer = c
            break

    if not customer:
        print("Customer Not Found!")
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

    qty = int(input("Enter Quantity: "))

    if qty > product["quantity"]:
        print("Insufficient Stock!")
        return

    total = qty * product["selling_price"]

    sale = {
        "customer_id": customer_id,
        "customer_name": customer["name"],
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": qty,
        "total": total
    }

    sales.append(sale)
    save_sales(sales)

    product["quantity"] -= qty
    save_products(products)

    print("Sale Recorded Successfully!")

def view_sales():
    sales = load_sales()

    if not sales:
        print("No Sales Found!")
        return

    table = []

    for s in sales:
        table.append([
            s["customer_id"],
            s["customer_name"],
            s["product_id"],
            s["product_name"],
            s["quantity"],
            s["total"]
        ])

    print(tabulate(
        table,
        headers=["Customer ID", "Customer", "Product ID", "Product", "Qty", "Total"],
        tablefmt="grid"
    ))
    
def sales_menu():
    while True:
        print("\n========== SALES MANAGEMENT ==========")
        print("1. Add Sale")
        print("2. View Sales")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_sale()

        elif choice == "2":
            view_sales()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")
