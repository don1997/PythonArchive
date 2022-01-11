class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Item: {self.name} Price: {self.price} Category: {self.category}"

Shovel = Item("shovel", 7.00, "Gardening")

print(Shovel.__str__())