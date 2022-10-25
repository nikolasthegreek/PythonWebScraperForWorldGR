from customers import Customer
import datetime
import db_manager

class BankAccount :
    
    # initialization at the moment just creates the data for the new object
    
    def __init__(self,customer):
        
        self.customer = customer
        self.openDate = datetime.date.today().strftime("%d/%m/%Y")
        self.status = "Active"
        self.acctype = "Deposit"
        
        
        
        
    def save (self):
        
        time_now = datetime.datetime.now()
        mstime = int(time_now.strftime("%f"));
        sead =((mstime*(int(self.customer.customer_id)*7))**0.5)/10
        self.iban = hash(sead)
        db_manager.InsertAccount(self.iban,self.customer.customer_id,self.openDate,self.status,self.acctype)



def CreateAccount(customer):
    
    
    acc = BankAccount(customer)
    acc.save()
    
    return acc


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   # main()
   #var = accountCreation(1,1)
   pass
