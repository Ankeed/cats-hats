# 1
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book: '{self.name}'")
        print(f"Author: {self.author}")
        print(f"Price: {self.price} UAH")
        print(f"Quantity: {self.quantity}")


book1 = Book("1984", 199.99, 50, "George Orwell")
book1.read()


# 2
class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name in self.menu and quantity <= self.menu[dish_name]['quantity']:
            total_cost = self.menu[dish_name]['price'] * quantity
            self.menu[dish_name]['quantity'] -= quantity
            return total_cost
        elif dish_name in self.menu and quantity > self.menu[dish_name]['quantity']:
            return "Requested quantity not available"
        else:
            return "Dont have that dish"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}
mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
