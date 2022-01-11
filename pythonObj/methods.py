#important note: Methods are functions inside classes
#unlike isolated def statements which are called functions

class Item:
    def calculate_total_price(self,x,y):
        return x * y

#creates instance of class
item1 = Item()

#assign attributes to instance of class
#do this by adding dot after class
item1.name = "phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price,item1.quantity))

#item2 is not defined if forget statement down below
item2 = Item()

item2.name = "laptop"
item2.price = 1000
item2.quantity = 3
print(item1.calculate_total_price(item2.price,item2.quantity))



