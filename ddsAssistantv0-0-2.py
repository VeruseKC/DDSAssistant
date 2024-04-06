import csv
import os
from datetime import datetime

# Constants
CLIENTS_FILE = 'clients.csv'
ORDERS_FILE = 'orders.csv'

# Helper Functions
def read_csv_to_list(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as file:
            if 'clients' in filepath:
                csv.writer(file).writerow(['Client Name'])
            elif 'orders' in filepath:
                csv.writer(file).writerow(['Timestamp', 'Client Name', 'Amount Requested', 'Packaging Options'])
        return []
    with open(filepath, 'r', newline='') as file:
        return list(csv.DictReader(file))

def append_to_csv(filepath, data, fieldnames):
    with open(filepath, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

def calculate_packaging(amount):
    packages = [1000, 500, 100, 50, 20, 10, 5, 3, 2, 1]
    result = []
    for pkg in packages:
        if amount >= pkg:
            num_pkg = amount // pkg
            amount -= num_pkg * pkg
            result.append(f"{num_pkg}x{pkg}g")
    return ', '.join(result)

# Main Functionalities
def add_client():
    name = input("Enter the new client's name: ")
    append_to_csv(CLIENTS_FILE, {'Client Name': name}, ['Client Name'])
    print(f"{name} added to client list.")

def list_clients():
    clients = read_csv_to_list(CLIENTS_FILE)
    if not clients:
        print("No clients available.")
        return
    print("\nClient List:")
    for client in clients:
        print(f"- {client['Client Name']}")

def new_order():
    clients = read_csv_to_list(CLIENTS_FILE)
    orders = []
    bag_summary = {}  # To store the summary of required bags

    for client in clients:
        try:
            amount = int(input(f"Enter the amount (in grams) {client['Client Name']} wants: "))
            packaging_options = calculate_packaging(amount)
            orders.append({'name': client['Client Name'], 'amount': amount, 'packaging': packaging_options})

            # Update bag summary
            for pkg_option in packaging_options.split(', '):
                num, size = pkg_option.split('x')
                size = size.strip('g')
                if size in bag_summary:
                    bag_summary[size] += int(num)
                else:
                    bag_summary[size] = int(num)

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            append_to_csv(ORDERS_FILE, {'Timestamp': timestamp, 'Client Name': client['Client Name'], 'Amount Requested': amount, 'Packaging Options': packaging_options}, ['Timestamp', 'Client Name', 'Amount Requested', 'Packaging Options'])
        except ValueError:
            print("Invalid amount entered, skipping.")

    if orders:
        print("\nOrders placed:")
        for order in orders:
            print(f"{order['name']} - {order['amount']}g: {order['packaging']}")

    # Display bag summary
    if bag_summary:
        print("\nBag Summary:")
        for size, count in bag_summary.items():
            print(f"{count} package(s) of {size}g")

def calculate_packaging(amount):
    packages = [1000, 500, 100, 50, 20, 10, 5, 3, 2, 1]
    result = []
    for pkg in packages:
        if amount >= pkg:
            num_pkg = amount // pkg
            amount -= num_pkg * pkg
            result.append(f"{num_pkg}x{pkg}")
    return ', '.join(result)
    
def order_history():
    orders = read_csv_to_list(ORDERS_FILE)
    if not orders:
        print("No order history available.")
        return
    print("\nOrder History:")
    for order in orders:
        print(f"{order['Timestamp']}: {order['Client Name']} - {order['Amount Requested']}g: {order['Packaging Options']}")

# Menu System
def main_menu():
    while True:
        print("\nDDS Assistant v0.0.2 By Veruse")
        print("\nMain Menu:")
        print("1. Clients")
        print("2. New Order")
        print("3. Order History")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            clients_menu()
        elif choice == '2':
            new_order()
        elif choice == '3':
            order_history()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def clients_menu():
    while True:
        print("\nClients Menu:")
        print("1. Add Client")
        print("2. List Clients")
        print("3. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_client()
        elif choice == '2':
            list_clients()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
