"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class CashRegister:

    def __init__(self):
        self.total_items = []
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        self.total_items.append(item)
        print(f"The item {item.name} was added to the cash register.")

    def remove_item(self, item):
        self.total_items.remove(item)
        print(f"The item {item.name} was successfully removed.")

    def apply_discount(self, discount):
        self.discount += discount
        print("Discount applied.")

    def get_total(self):
        self.total_price = 0
        for item in self.total_items:
            self.total_price = self.total_price + item.price
        self.total_price = self.total_price - self.discount
        self.total_price = max(self.total_price, 0)
        return self.total_price

    def show_items(self):
        print("The items in the cash register are:")
        for item in self.total_items:
            print(f"- {item.name.capitalize()} \t £{item.price:.2f}")

    def reset_register(self):
        self.total_items = []
        self.total_price = 0
        self.discount = 0
        print("Register reset.")


# EXAMPLE code run:

shop_register = CashRegister()
print(f"Items so far: {shop_register.total_items}")

bread = Item("bread", 1.00)
broccoli = Item("broccoli", 0.70)
cheese = Item("cheese", 3.00)

shop_register.add_item(bread)
shop_register.add_item(broccoli)
shop_register.add_item(cheese)
shop_register.show_items()
print(f"Total so far: £{shop_register.get_total():.2f}")
shop_register.apply_discount(2.00)
print(f"Total after discount: £{shop_register.get_total():.2f}")
shop_register.remove_item(broccoli)
shop_register.show_items()
shop_register.reset_register()
