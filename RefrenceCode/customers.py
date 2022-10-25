import db_manager

class Customer :

    def __init__(self, name,surname,dateofbirth):
        
        self.custid= None
        self.name = name
        self.surname = surname
        self.dateofbirth = dateofbirth
        
        
    def save(self):
        
        self.customer_id = db_manager.InsertCustomer(self.name, self.surname, self.dateofbirth)
    
    
def GetCustomer(custid):
    
    tempcustomer = db_manager.getcustomer(custid)
    c = Customer(tempcustomer[1],tempcustomer[2], tempcustomer[3])
    c.customer_id = custid
    print("custid set to"+custid);
    
    return c


def CreateCustomer (name,surname,dateofbirth):
    
    c = Customer (name,surname,dateofbirth)
    c.save()
    
    return c





   
