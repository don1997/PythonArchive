#SUMMARY
"""
Essentially this lesson was about the problem
of representing all of the objects within our class
to do this you have two options
I have marked down below the options
Basically you can use a for loop or a magic method to achieve this 

"""
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    #BOTH 1 and 2
    all = []

    def __init__(self, name: str ,price: float,quantity = 0):
        print(f"An instance created: {name}")
                        
        assert price >= 0, f"Price {price} is not greater than 0 or equal to"
        assert quantity >= 0,  f"Price {quantity} is not greater than 0 or equal to"

        self.name = name
        self.price = price
        self.quantity = quantity
        #BOTH 1 and 2
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    #OPTION 2
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#OPTION 1
for instance in Item.all:
    print(instance.name)
#OPTION 2
print(Item.all)

