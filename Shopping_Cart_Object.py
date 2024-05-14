# Defined class name as Cart
class Cart:

    # Initialized (attribute)
    def __init__(self):
        self.items = {}
        self.price_list = {"Mobile": 1000, "Laptop": 2000, "Headphone": 500}
        self.total = 0

    # Defined adding items to cart (method)
    def add_items(self, product, quantity):
        self.items[product] = quantity

    # Defined removing items from cart (method)
    def remove_items(self, product):
        del self.items[product]

    # Defined updating items in cart (method)
    def update_items(self, product, new_quantity):
        self.items[product] = new_quantity

    # Defined showing items in cart (method)
    def show_cart_items(self):
        print(list(self.items.items()))

    # Defined total sum of items in cart (method)
    def total_of_cart(self):
        for item, quantity in self.items.items():
            self.total += quantity * self.price_list[item]
        print(self.total)


cart_obj = Cart()

# Adding items in cart:
cart_obj.add_items(input('Enter the item name : '), int(input('Enter the quantity of the item : ')))
cart_obj.add_items("Mobile", 2)
cart_obj.add_items("Headphone", 3)

cart_obj.show_cart_items()

# Updating items in cart:

cart_obj.update_items("Mobile", 5)
cart_obj.update_items("Laptop", 2)
cart_obj.update_items("Book", 7)

cart_obj.show_cart_items()

# Removing items in cart

cart_obj.remove_items("Book")

cart_obj.show_cart_items()

# Calculating total MRP of items in cart

cart_obj.total_of_cart()
