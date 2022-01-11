#OOP PROJECT python
#TASK: Build a program to calculate total cost of food on menu
#      for restaurant.

class Customer:
    def __init__(self, name, item):
        self.name   = name
        self. item  = item
    
    def getTotal(self):
        pass

class Order:
    def __init__(self, name, item)
    self. item  = item
  
        
#menu
menu = ["burger", "pizza", "soda"]

prices = [10, 17, 3]

#total init
total = 0
#while loop init
alpha = True

#USER IN
cust_name = input("What is your name?: ")

while alpha:

    #checks to see if item is in menu   START
    proceed = False
    while not proceed:
        cust_item = input("what is your item?: ")
        if cust_item in menu:
            print("proceed")
            
            temp = cust_item
            
            item_index = menu.index(temp)
            
            proceed = True
        
        else: 
            print("Item does not exist")
    #checks to see if item is in menu   END

    #aligns item index with price index to get item price
    item_price = prices[item_index]

    #OBJECT assign
    customer_1 = Customer(cust_name, cust_item)

    #print(customer_1.name, customer_1.item)
    
    #assigs total to prices list
    total += prices[item_index]
    
    #does user wish to leave?
    proceed = input("do you whis to exit? y/n: ")

    if(proceed == 'y'):
        alpha = False
    else:
        pass

print("the total is : $" + str(total))
