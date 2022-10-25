import accounts
import customers

def mainmenu():
    
    
    q1 = input ("Enter your selection (1/Create Account  9/Exit): ")
 
    if int(q1) == 1:
        
        SelectCreateAccount ()
         
    
    
def SelectCreateAccount ():
    q2 = Sign_in_or_up ()
        
    if q2 =="new":
            
        customer = Customer_Creation_Request()
        account = Account_Creation_Request (customer)
        print("your bank ID is =",account.acctid)
        
        
    else:
        
        Account_Creation_Request(None)
    
    
    


def Sign_in_or_up ():
    
    while True :
        
        q2 = input ("new or existing customer( new or existing ):")
        
        if q2=="new"or q2=="existing" :
            
            break
    
    return q2

#-----------------------------

def Customer_Creation_Request ():
    
    name = input ("name :")
    surname = input ("surname :")
    dateofbirth = input ("date of birth (DD/MM/YYYY):")
    customer = customers.CreateCustomer (name,surname,dateofbirth)
    
    
    return customer



def Account_Creation_Request (customer):
    
    if customer==None :
        
        custid = input ("your bank ID :")
        customer = customers.GetCustomer(custid)
        
    acc = accounts.CreateAccount (customer)
    
    return acc




#==========================================================================================================================================================================================
#                                                                                            START
#==========================================================================================================================================================================================
mainmenu()


