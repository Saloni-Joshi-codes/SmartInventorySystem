import json
from tabulate import tabulate

BILL_FILE = "data/bills.json"
SALES_FILE = "data/sales.json"

def load_bills():
    try:
        with open(BILL_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_bills(bills):
    with open(BILL_FILE, "w") as file:
        json.dump(bills, file, indent=4)

def load_sales():
    try:
        with open(SALES_FILE, "r") as file:
            return json.load(file)
    except:
        return []
    
def generate_bill():
    sales = load_sales()
    bills = load_bills()

    if not sales:
        print("No Sales Found!")
        return

    sale = sales[-1]

    bill = {
        "customer": sale["customer_name"],
        "product": sale["product_name"],
        "quantity": sale["quantity"],
        "total": sale["total"]
    }

    bills.append(bill)
    save_bills(bills)

    print("\n========== CUSTOMER BILL ==========")
    print(f"Customer : {bill['customer']}")
    print(f"Product  : {bill['product']}")
    print(f"Quantity : {bill['quantity']}")
    print(f"Total    : ₹{bill['total']}")
    print("===================================")

def view_bills():
    bills = load_bills()

    if not bills:
        print("No Bills Found!")
        return

    table = []

    for b in bills:
        table.append([
            b["customer"],
            b["product"],
            b["quantity"],
            b["total"]
        ])

    print(tabulate(
        table,
        headers=["Customer", "Product", "Qty", "Total"],
        tablefmt="grid"
    ))

def billing_menu():
    while True:
        print("\n========== BILLING ==========")
        print("1. Generate Bill")
        print("2. View Bills")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            generate_bill()
        elif choice == "2":
            view_bills()
        elif choice == "0":
            break
        else:
            print("Invalid Choice!")