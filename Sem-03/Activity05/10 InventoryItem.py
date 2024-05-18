class InventoryItem:
    def __init__(self, product_id, name, initial_quantity):
        self.__product_id = product_id
        self.__name = name
        self.__stock_quantity = initial_quantity

    def get_stock_level(self):
        return self.__stock_quantity

    def sell_item(self, quantity):
        if 0 < quantity <= self.__stock_quantity:
            self.__stock_quantity -= quantity
            print(f"Sold {quantity} of {self.__name}. New stock level: {self.__stock_quantity}")
        else:
            print("Invalid quantity. Cannot sell more than available stock.")

item = InventoryItem("P12345", "Widget", 50)
print(item.get_stock_level())

item.sell_item(10)
print(item.get_stock_level())

item.sell_item(50)
print(item.get_stock_level())
