
class Item:

    #note
    def __init__(self, name: str ,price: float,quantity = 0):
        print(f"An instance created: {name}")
        #run validations to the recived arguments
        #makes sure object is greater than 0                     #for insertion error
        assert price >= 0, f"Price {price} is not greater than 0 or equal to"
        assert quantity >= 0,  f"Price {quantity} is not greater than 0 or equal to"



        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    #notice no need for parameters and x and y vars
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())