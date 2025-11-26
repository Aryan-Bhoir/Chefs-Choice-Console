# ---------------------------------------------------------
# Chef’s Choice Console
# ---------------------------------------------------------

class MenuItem:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self.items = {
            1: MenuItem(1, "Pizza", 180),
            2: MenuItem(2, "Burger", 120),
            3: MenuItem(3, "Pasta", 150),
            4: MenuItem(4, "French Fries", 80),
            5: MenuItem(5, "Cold Drink", 40)
        }

    def show_menu(self):
        print("\n========== MENU ==========")
        for code, item in self.items.items():
            print(f"{code}. {item.name} - ₹{item.price}")
        print("==========================\n")

    def add_item(self, name, price):
        new_code = max(self.items.keys()) + 1
        self.items[new_code] = MenuItem(new_code, name, price)
        print(f"Item '{name}' added successfully!")

    def remove_item(self, code):
        if code in self.items:
            removed = self.items.pop(code)
            print(f"Item '{removed.name}' removed!")
        else:
            print("Invalid code!")


class Order:
    def __init__(self, customer_name, table_number):
        self.customer_name = customer_name
        self.table_number = table_number
        self.ordered_items = []

    def add_item(self, item, qty):
        self.ordered_items.append([item, qty])

    def is_empty(self):
        return len(self.ordered_items) == 0


class Bill:
    def __init__(self, order):
        self.order = order

    def generate_bill(self):
        print("\n=================== BILL ===================")
        print(f"Customer Name : {self.order.customer_name}")
        print(f"Table Number  : {self.order.table_number}")
        print("-------------------------------------------")

        total = 0
        for item, qty in self.order.ordered_items:
            item_total = item.price * qty
            total += item_total
            print(f"{item.name} x {qty} = ₹{item_total}")

        print("-------------------------------------------")
        print(f"Subtotal           : ₹{total}")

        # GST 5%
        gst = total * 0.05
        final_amount = total + gst

        print(f"GST (5%)           : ₹{gst:.2f}")
        print("-------------------------------------------")
        print(f"Total Payable      : ₹{final_amount:.2f}")
        print("===========================================\n")


class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self):
        print("\n===== ADMIN LOGIN =====")
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == self.username and pwd == self.password:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials!\n")
            return False


class RestaurantSystem:
    def __init__(self):
        self.menu = Menu()
        self.admin = Admin()

    def take_order(self):
        name = input("Enter customer name: ")
        table = input("Enter table number: ")

        order = Order(name, table)

        while True:
            try:
                self.menu.show_menu()
                code = int(input("Enter item code (0 to finish): "))
                if code == 0:
                    break

                if code not in self.menu.items:
                    print("Invalid code!")
                    continue

                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("Quantity must be > 0!")
                    continue

                order.add_item(self.menu.items[code], qty)
                print("Item added!")

            except ValueError:
                print("Enter valid numbers!")

        if order.is_empty():
            print("No items ordered!")
            return

        bill = Bill(order)
        bill.generate_bill()

    def admin_panel(self):
        if not self.admin.login():
            return

        while True:
            print("\n===== ADMIN MENU =====")
            print("1. Add Food Item")
            print("2. Remove Food Item")
            print("3. Show Menu")
            print("4. Back to Main Menu")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter food name: ")
                price = int(input("Enter price: "))
                self.menu.add_item(name, price)

            elif choice == "2":
                self.menu.show_menu()
                code = int(input("Enter item code to remove: "))
                self.menu.remove_item(code)

            elif choice == "3":
                self.menu.show_menu()

            elif choice == "4":
                break

            else:
                print("Invalid choice!")

    def main_menu(self):
        while True:
            print("\n======== RESTAURANT SYSTEM ========")
            print("1. Customer Order")
            print("2. Admin Panel")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.take_order()

            elif choice == "2":
                self.admin_panel()

            elif choice == "3":
                print("Thank you! Visit Again.")
                break

            else:
                print("Invalid choice! Try again.")


# Run Program
restaurant = RestaurantSystem()
restaurant.main_menu()
