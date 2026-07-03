from authentication import login
from product import product_menu
from inventory import inventory_menu
from supplier import supplier_menu 
from customer import customer_menu
from sales import sales_menu
from purchase import purchase_menu
from billing import billing_menu

def menu():
    while True:
        print("\n" + "=" * 45)
        print(" SMART INVENTORY MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Product Management")
        print("2. Inventory Management")
        print("3. Supplier Management")
        print("4. Customer Management")
        print("5. Sales")
        print("6. Purchase")
        print("7. Billing")
        print("8. Reports")
        print("9. Logout")
        print("0. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Thank you for using Smart Inventory System.")
            break
        elif choice == "9":
            print("Logged Out Successfully.")
            break
        elif choice == "1":
          product_menu()

        elif choice == "2":
            inventory_menu()
        
        elif choice == "3":
            supplier_menu()

        elif choice == "4":
            customer_menu()

        elif choice == "5":
            sales_menu()
        
        elif choice == "6":
            purchase_menu()

        elif choice == "7":
            billing_menu()
            
        elif choice == "8":
              print("This module will be developed next.")
        
        else:
            print("Invalid Choice!")

if login():
    menu()
