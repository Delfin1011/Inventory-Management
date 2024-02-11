from prettytable import PrettyTable
from colorama import Fore, Style, init
from datetime import datetime, timedelta

class InventoryManagement:
    def __init__(self):
        init()
        self.inventory = {}

    def add_item(self, id, name, quantity, unit, expiration_date):
        if id in self.inventory:
            print(Fore.RED + "Error: ID already exists." + Style.RESET_ALL)
            return False
        self.inventory[id] = {"Name": name, "Quantity": quantity, "Unit": unit, "ExpirationDate": expiration_date, "StockIn": [], "StockOut": []}
        self.record_stock_in(id, quantity)
        print(Fore.GREEN + "Item added successfully." + Style.RESET_ALL)
        return True

    def record_stock_in(self, id, quantity):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inventory[id]["StockIn"].append({"Date": date, "Quantity": quantity})
        print(Fore.GREEN + f"Stocked in {quantity} units on {date}." + Style.RESET_ALL)

    def record_stock_out(self, id, quantity):
        if self.inventory[id]["Quantity"] < quantity:
            print(Fore.RED + "Error: Insufficient stock." + Style.RESET_ALL)
            return False
        self.inventory[id]["Quantity"] -= quantity
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inventory[id]["StockOut"].append({"Date": date, "Quantity": quantity})
        print(Fore.GREEN + f"Stocked out {quantity} units on {date}." + Style.RESET_ALL)
        return True

    def display_almost_expired(self):
        threshold_date = datetime.now() + timedelta(days=30)
        table = PrettyTable([Fore.LIGHTYELLOW_EX + "ID", "Name", "Quantity", "Unit", "Expiration Date", "Days Until Expiry" + Style.RESET_ALL])
        for id, info in self.inventory.items():
            expiration_date = datetime.strptime(info["ExpirationDate"], "%Y-%m-%d")
            days_until_expiry = (expiration_date - datetime.now()).days
            if days_until_expiry <= 365:
                table.add_row([id, info["Name"], info["Quantity"], info["Unit"], info["ExpirationDate"], days_until_expiry])
        print(table)

    def update_item(self):
        while True:
            id = input(Fore. YELLOW + "Enter the ID of the item you wish to update: "+ Style. RESET_ALL)
            if id not in self.inventory:
                print(Fore.RED + "Error: ID does not exist. Please try again." + Style.RESET_ALL)
                continue

            print(Fore. YELLOW + "What would you like to update?"+ Style. RESET_ALL)
            print(Fore. CYAN + "1. Name"+ Style. RESET_ALL)
            print(Fore. CYAN + "2. Quantity"+ Style. RESET_ALL)
            print(Fore. CYAN + "3. Unit"+ Style. RESET_ALL)
            print(Fore. CYAN + "4. Expiration Date"+ Style. RESET_ALL)
            update_choice = input("Enter your choice (1/2/3/4): ")

            if update_choice == "1":
                new_name = input("Enter new Name: ")
                self.inventory[id]["Name"] = new_name
            elif update_choice == "2":
                new_quantity = int(input("Enter new Quantity: "))
                self.inventory[id]["Quantity"] = new_quantity
            elif update_choice == "3":
                new_unit = input("Enter new Unit: ")
                self.inventory[id]["Unit"] = new_unit
            elif update_choice == "4":
                new_expiration_date = input("Enter new Expiration Date (YYYY-MM-DD): ")
                self.inventory[id]["ExpirationDate"] = new_expiration_date
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue

            print(Fore.GREEN + "Item updated successfully." + Style.RESET_ALL)
            break

    def delete_item(self):
        while True:
            id = input(Fore. YELLOW + "Enter the ID of the item you wish to delete: "+ Style. RESET_ALL)
            if id not in self.inventory:
                print(Fore.RED + "Error: ID does not exist. Please try again." + Style.RESET_ALL)
                continue

            del self.inventory[id]
            print(Fore.GREEN + "Item deleted successfully." + Style.RESET_ALL)
            break

    def display_inventory(self):
        table = PrettyTable([Fore.LIGHTYELLOW_EX + "ID", "Name", "Quantity", "Unit", "Expiration Date" + Style.RESET_ALL])
        for id, info in self.inventory.items():
            table.add_row([id, info["Name"], info["Quantity"], info["Unit"], info["ExpirationDate"]])
        print(table)

    def display_stock_in_history(self, id):
        if id not in self.inventory:
            print(Fore.RED + "Error: ID does not exist." + Style.RESET_ALL)
            return
        table = PrettyTable([Fore.LIGHTYELLOW_EX + "Date", "Quantity Stocked In" + Style.RESET_ALL])
        for log in self.inventory[id]["StockIn"]:
            table.add_row([log["Date"], log["Quantity"]])
        print(table)

    def display_stock_out_history(self, id):
        if id not in self.inventory:
            print(Fore.RED + "Error: ID does not exist." + Style.RESET_ALL)
            return
        table = PrettyTable([Fore.LIGHTYELLOW_EX + "Date", "Quantity Stocked Out" + Style.RESET_ALL])
        for log in self.inventory[id]["StockOut"]:
            table.add_row([log["Date"], log["Quantity"]])
        print(table)


    def id_exists(self, id):
        return id in self.inventory

    def stock_in(self):
        id = input(Fore. YELLOW + "Enter the ID for stock in: "+ Style. RESET_ALL)
        if not self.id_exists(id):
            print(Fore.RED + "Error: ID does not exist." + Style.RESET_ALL)
            return
        quantity = input(Fore . CYAN + "Enter Quantity for stock in: "+ Style. RESET_ALL)
        try:
            quantity = int(quantity)
        except ValueError:
            print(Fore.RED + "Error: Quantity should be an integer." + Style.RESET_ALL)
            return
        self.record_stock_in(id, quantity)
        self.inventory[id]["Quantity"] += quantity
     


    def stock_out(self):
        id = input(Fore. YELLOW + "Enter the ID for stock out: "+ Style. RESET_ALL)
        if not self.id_exists(id):
            print(Fore.RED + "Error: ID does not exist." + Style.RESET_ALL)
            return
        quantity = input(Fore. CYAN + "Enter Quantity for stock out: "+ Style. RESET_ALL)
        try:
            quantity = int(quantity)
        except ValueError:
            print(Fore.RED + "Error: Quantity should be an integer." + Style.RESET_ALL)
            return
        if self.record_stock_out(id, quantity):
            print(Fore.GREEN + "Stock out recorded successfully." + Style.RESET_ALL)

def main():
    manager = InventoryManagement()
    while True:
        print(Fore.LIGHTMAGENTA_EX + "\nInventory Management System" + Style.RESET_ALL)
        print("1. Add Product")
        print("2. Display Inventory")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Stock In")
        print("6. Stock Out")
        print("7. Display Stock In History")
        print("8. Display Stock Out History")
        print("9. Display Almost Expired Products")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
             while True:
              id = input(Fore. CYAN + "Enter ID: "  + Style. RESET_ALL)
              if manager.id_exists(id):
                   print(Fore.RED + "Error: ID already exists. Please use a different ID." + Style.RESET_ALL)
              else:
                break  
        
             name = input(Fore. CYAN + "Enter Name: " + Style. RESET_ALL)
             quantity = input(Fore. CYAN + "Enter Quantity: " + Style. RESET_ALL)
             while True:
                try:
                    quantity = int(quantity)
                    break
                except ValueError:
                    print(Fore.RED + "Error: Quantity should be an integer. Please enter a valid quantity." + Style.RESET_ALL)
                    quantity = input(Fore. CYAN + "Enter Quantity: "+ Style. RESET_ALL)
             unit = input(Fore.CYAN +"Enter Unit: " + Style. RESET_ALL)
             expiration_date = input(Fore.CYAN +"Enter Expiration Date (YYYY-MM-DD): "+ Style. RESET_ALL)
             manager.add_item(id, name, quantity, unit, expiration_date)

        elif choice == "2":
            manager.display_inventory()

        elif choice == "3":
            manager.update_item()

        elif choice == "4":
            manager.delete_item()
            
        elif choice == "5":
            manager.stock_in()
           
        elif choice == "6":
            manager.stock_out()
           
        elif choice == "7":
            id = input(Fore . YELLOW + "Enter the ID to display stock in history: "+ Style.RESET_ALL)
            manager.display_stock_in_history(id)
           
        elif choice == "8":
            id = input(Fore. YELLOW + "Enter the ID to display stock out history: "+ Style.RESET_ALL)
            manager.display_stock_out_history(id)
           
        elif choice == "9":
            manager.display_almost_expired()
        elif choice == "10":
            print(Fore.BLACK + "Exiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
