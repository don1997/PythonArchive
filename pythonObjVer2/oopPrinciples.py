class User:
    def log(self): 
        print(self)

class Teacher(User):
    def log(self):
        print("I am a teacher!")
        

class Customer(User):
    def __init__(self,name,membership_type):
        self.name = name 
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        print("calculated costs")
        self.membership_type = new_membership

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

    #print all customer
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    #make name a property
    #so we will create two methods below
    @property
    def name(self):
        #print("getting name")
        return self._name
    
    @name.setter
    def name(self, name):
        #print("settng name")
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    #compare attributes
    def __eq__(self,other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __hash__ = None

    __repr__ = __str__
    
users = [Customer("Caleb", "Gold"), 
         Customer("John", "Silver"),
         Teacher()
        ]
for user in users:
    user.log()


