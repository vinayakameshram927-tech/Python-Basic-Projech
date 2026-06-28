inventory = {}

# Load inventory from file
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                pid, name, category, price, qty, reorder = line.strip().split(",")
                inventory[pid] = {
                    "name": name,
                    "category": category,
                    "price": float(price),
                    "qty": int(qty),
                    "reorder": int(reorder)
                }
    except FileNotFoundError:
        pass


# Save inventory to file
def save_inventory():
    with open("inventory.txt", "w") as file:
        for pid, p in inventory.items():
            file.write(f"{pid},{p['name']},{p['category']},{p['price']},{p['qty']},{p['reorder']}\n")


# Add product
def add_product():
    pid = input("Product ID: ")

    if pid in inventory:
        print("Product ID already exists!")
        return

    name = input("Product Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    reorder = int(input("Reorder Level: "))

    inventory[pid] = {
        "name": name,
        "category": category,
        "price": price,
        "qty": qty,
        "reorder": reorder
    }

    print("Product Added Successfully!")


# Stock In
def stock_in():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        qty = int(input("Quantity to Add: "))
        inventory[pid]["qty"] += qty
        print("Stock Updated!")
    else:
        print("Product Not Found!")


# Stock Out
def stock_out():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        qty = int(input("Quantity to Remove: "))

        if inventory[pid]["qty"] >= qty:
            inventory[pid]["qty"] -= qty
            print("Stock Removed!")
        else:
            print("Insufficient Stock!")
    else:
        print("Product Not Found!")


# View Inventory
def view_inventory():
    print("\nID\tName\tQty\tPrice")
    print("-" * 40)

    for pid, p in inventory.items():
        print(pid, p["name"], p["qty"], p["price"], sep="\t")


# Low Stock Alert
def low_stock_alert():
    print("\nLow Stock Products:")

    for pid, p in inventory.items():
        if p["qty"] <= p["reorder"]:
            print(pid, "-", p["name"])


# Report
def generate_report():
    total_value = 0
    categories = set()

    for p in inventory.values():
        total_value += p["price"] * p["qty"]
        categories.add(p["category"])

    print("\n===== REPORT =====")
    print("Total Products :", len(inventory))
    print("Total Value    :", total_value)
    print("Categories     :", ", ".join(categories))


# Main Program
load_inventory()

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        stock_in()
    elif choice == "3":
        stock_out()
    elif choice == "4":
        view_inventory()
    elif choice == "5":
        low_stock_alert()
    elif choice == "6":
        generate_report()
    elif choice == "7":
        save_inventory()
        print("Data Saved. Exiting...")
        break
    else:
        print("Invalid Choice!")
