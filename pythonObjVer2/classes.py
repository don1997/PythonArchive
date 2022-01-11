class Customer:
    def __init__(self,name,membership_type):
        self.name = name 
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

    def read_customer():
        print("Reading customer from DB")

    #print all customer
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    #compare attributes
    def __eq__(self,other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __hash__ = None

    __repr__ = __str__
    
customers = [Customer("Caleb", "Gold"), 
             Customer("Caleb", "Gold")]



print(customers[0] == customers[1])


