#methods with __ex__ are called magic methods

class Item:
    #This method does: When python creates an instance of a class
    # ex item1 = item()
    # then python executes the init method automatically
    #basically everytime an instance of a class is init
    #def_init__(self) is called

    #to avoid hardcoding attributes for each instance
    def __init__(self, name,price,quantity):
        print(f"An instance created: {name}")
        #dynamic attribute assignment
        #use this instead of hardcoding attributes
        #from before
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self,x,y):
        return x * y

#creates instance of class
item1 = Item("Phone", 100, 5)

#assign attributes to instance of class
#do this by adding dot after class


#item2 is not defined if forget statement down below
item2 = Item("Laptop", 1000, 3)


