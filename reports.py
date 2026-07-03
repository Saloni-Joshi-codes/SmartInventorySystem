import json
from tabulate import tabulate

PRODUCT_FILE = "data/products.json"
SALES_FILE = "data/sales.json"


def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def load_sales():
    try:
        with open(SALES_FILE, "r") as file:
            return json.load(file)
    except:
        return []
    
def total_sales():
    sales = load_sales()

    total = sum(s["total"] for s in sales)

    print("\n========== TOTAL SALES ==========")
    print(f"Total Sales : ₹{total}")


def best_selling_product():
    sales = load_sales()

    if not sales:
        print("No Sales Found!")
        return

    products = {}

    for sale in sales:
        name = sale["product_name"]

        if name not in products:
            products[name] = 0

        products[name] += sale["quantity"]

    best = max(products, key=products.get)

    print("\n====== BEST SELLING PRODUCT ======")
    print(f"Product : {best}")
    print(f"Units Sold : {products[best]}")

def profit_report():
    products = load_products()
    sales = load_sales()

    revenue = sum(s["total"] for s in sales)

    cost = 0

    for sale in sales:
        for product in products:
            if product["id"] == sale["product_id"]:
                cost += product["cost_price"] * sale["quantity"]

    profit = revenue - cost

    print("\n========== PROFIT REPORT ==========")
    print(f"Revenue : ₹{revenue}")
    print(f"Cost    : ₹{cost}")
    print(f"Profit  : ₹{profit}")

def inventory_report():

    products = load_products()

    if not products:
        print("No Products Available!")
        return

    table = []

    total_products = len(products)
    total_stock = 0
    inventory_value = 0

    for product in products:
        total_stock += product["quantity"]
        inventory_value += product["quantity"] * product["cost_price"]

        table.append([
            product["id"],
            product["name"],
            product["category"],
            product["quantity"]
        ])

    print("\n========== INVENTORY REPORT ==========\n")

    print(tabulate(
        table,
        headers=["ID","Product","Category","Stock"],
        tablefmt="grid"
    ))

    print(f"\nTotal Products : {total_products}")
    print(f"Total Stock    : {total_stock}")
    print(f"Inventory Value: ₹{inventory_value}")

def category_report():

    products = load_products()

    category = {}

    for product in products:

        if product["category"] not in category:
            category[product["category"]] = 0

        category[product["category"]] += 1

    print("\n====== CATEGORY REPORT ======")

    for key, value in category.items():
        print(f"{key} : {value} Products")

def reports_menu():

    while True:

        print("\n========== REPORTS ==========")
        print("1. Total Sales")
        print("2. Best Selling Product")
        print("3. Profit Report")
        print("4. Inventory Report")
        print("5. Category Report")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            total_sales()

        elif choice == "2":
            best_selling_product()

        elif choice == "3":
            profit_report()

        elif choice == "4":
            inventory_report()

        elif choice == "5":
            category_report()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")