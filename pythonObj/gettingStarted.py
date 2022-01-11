class Item:
    pass

#creates instance of class
item1 = Item()

#assign attributes to instance of class
#do this by adding dot after class
item1.name = "phone"
item1.price = 100
item1.quantity = 5

print(type(item1)) #item
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int

#note how item1 is an item data type

