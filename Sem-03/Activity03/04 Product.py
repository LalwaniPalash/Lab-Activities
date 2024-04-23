class Product:
    tax_rate = 0.1

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount
        print(f"Added {amount} units of {self.name}. New quantity: {self.quantity}")

    def sell_item(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} units of {self.name}. New quantity: {self.quantity}")
        else:
            print("Error: Insufficient quantity available")

    def calculate_total_cost(self):
        total_cost = self.price * self.quantity
        total_cost_with_tax = total_cost * (1 + self.tax_rate)
        return total_cost_with_tax

    @classmethod
    def set_tax_rate(cls, tax_rate):
        cls.tax_rate = tax_rate

product1 = Product("Book", 10, 50)

product1.add_stock(20)

product1.sell_item(15)

total_cost = product1.calculate_total_cost()

print(f"Total cost including tax: ${total_cost:.2f}")
